from rest_framework import serializers
from .models import Task, Profile, Category
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()  # Nested One-to-One relationship
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())  # One-to-Many relationship

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'tasks']

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # One-to-Many relationship
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())  # Use this for ID-based input

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date', 'user', 'categories']
