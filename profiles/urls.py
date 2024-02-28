from django.urls import path
from .views import SentenceGeneratorView,UserProfileListCreateView, UserProfileRetrieveUpdateDestroyView,upload_profile_picture,PostListCreateView,CategoryListView,SubcategoryListCreateView, PostRetrieveUpdateDestroyView, CommandCreateView, CommandDestroyView,CommandListView

urlpatterns = [
    path('sentence-generator/', SentenceGeneratorView.as_view(), name='sentence-generator'),
    path('profiles/', UserProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyView.as_view(), name='profile-retrieve-update-destroy'),
    path('profiles/upload/<int:user_id>/', upload_profile_picture, name='upload-profile-picture'),
     path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    path('posts/<int:post_id>/commands/', CommandListView.as_view(), name='command-list'),
    path('posts/<int:post_id>/commands/create/', CommandCreateView.as_view(), name='command-create'),
    path('posts/<int:post_id>/commands/<int:command_id>/', CommandDestroyView.as_view(), name='command-destroy'),
     path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/subcategories/', SubcategoryListCreateView.as_view(), name='subcategory-list-create'),

]