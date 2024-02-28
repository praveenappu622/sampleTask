from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import UserProfile
from .serializers import UserProfileSerializer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from .tasks import process_profile_picture
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer, PostSerializer, CommandSerializer,SubcategorySerializer
from .static_data import CATEGORIES
from .models import Category, Subcategory,PostModel, CommandModel
from django.views.generic import TemplateView
from django.shortcuts import render

class SentenceGeneratorView(TemplateView):
    template_name = 'sentence_generator.html'

class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    template_name = 'profile_list.html'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        sentence = f"New user profile created: {response.data['name']}"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("real_time", {"type": "real_time.message", "message": sentence})
        return response

class UserProfileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    template_name = 'profile_detail.html'

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        sentence = f"User profile updated: {response.data['name']}"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("real_time", {"type": "real_time.message", "message": sentence})
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        sentence = f"User profile deleted: {instance.name}"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("real_time", {"type": "real_time.message", "message": sentence})
        return response
    
def upload_profile_picture(request, user_id):
    try:
        # Assuming 'profile_picture' is the name of the file input in your HTML form
        uploaded_file = request.FILES['profile_picture']
        file_path = f"media/{uploaded_file.name}"  # Save the uploaded file to the media directory

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Call the Celery task asynchronously
        result = process_profile_picture.delay(file_path, user_id)

        return HttpResponse(f"Profile picture processing started. Task ID: {result.id}")
    except KeyError:
        return HttpResponse("Profile picture not provided in the request.", status=400)
    except Exception as e:
        return HttpResponse(f"Error processing profile picture: {str(e)}", status=500)
    

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            return Category.objects.filter(id=category_id)
        else:
            return Category.objects.all()

class SubcategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            return Subcategory.objects.filter(category__id=category_id)
        else:
            return Subcategory.objects.all()

    def perform_create(self, serializer):
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        serializer.save(category=category)


class PostListCreateView(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

class CommandListView(generics.ListAPIView):
    queryset = CommandModel.objects.all()
    serializer_class = CommandSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return CommandModel.objects.filter(post__id=post_id)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    def perform_destroy(self, instance):
        # Delete the post if all commands are deleted
        if instance.commands.count() == 0:
            instance.delete()

class CommandCreateView(generics.CreateAPIView):
    queryset = CommandModel.objects.all()
    serializer_class = CommandSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = PostModel.objects.get(id=post_id)
        serializer.save(post=post)

class CommandDestroyView(generics.DestroyAPIView):
    queryset = CommandModel.objects.all()
    serializer_class = CommandSerializer
    lookup_url_kwarg = 'command_id'
    def perform_destroy(self, instance):
        post = instance.post
        instance.delete()
        if post.commands.count() == 0:
            post.delete()
    
def create_sample_data():
    programming_category = Category.objects.create(name='Programming')
    Subcategory.objects.create(category=programming_category, name='Python')
    Subcategory.objects.create(category=programming_category, name='JavaScript')
    Subcategory.objects.create(category=programming_category, name='Java')

    cooking_category = Category.objects.create(name='Cooking')
    Subcategory.objects.create(category=cooking_category, name='Italian')
    Subcategory.objects.create(category=cooking_category, name='Baking')
    Subcategory.objects.create(category=cooking_category, name='Grilling')

#create_sample_data()

