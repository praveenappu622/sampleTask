from rest_framework import serializers
from .models import UserProfile,Category, Subcategory,PostModel, CommandModel

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'profile_picture']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandModel
        fields = ['id', 'command', 'publication_date']

class PostSerializer(serializers.ModelSerializer):
    commands = CommandSerializer(many=True, read_only=True)
    total_commands = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = ['id', 'title', 'author', 'created_at', 'commands', 'total_commands']

    def get_total_commands(self, obj):
        return obj.commands.count()
