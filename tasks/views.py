from rest_framework import generics, filters
from .models import Task, Profile, Category
from .serializers import TaskSerializer, ProfileSerializer, CategorySerializer, UserSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone           # For timezone filtering
from django.db.models import Count          # For task count aggregation

# Custom Pagination Class
class TaskPagination(PageNumberPagination):
    page_size = 5

# List all Tasks or Create a new Task
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'due_date']  # Filter by status or due date
    search_fields = ['title', 'description']  # Search by title or description
    pagination_class = TaskPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign the logged-in user to the task

# Retrieve, Update, or Delete a Task
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# List Overdue Tasks (due_date is in the past and status is 'pending')
class TaskListOverdue(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(due_date__lt=timezone.now(), status='pending')

# List or Create Categories
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# List User Profiles
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# List users with their task counts
class UserTaskCount(generics.ListAPIView):
    queryset = User.objects.annotate(task_count=Count('tasks'))
    serializer_class = UserSerializer

# List tasks for the logged-in user or create a new task
class TaskListUser(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
