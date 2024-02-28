
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PostModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or str(self.id)

class CommandModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='commands')
    command = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.command

