from django.urls import path
from .views import TaskListCreate, TaskDetail, TaskListOverdue, UserTaskCount, CategoryListCreate, ProfileList, TaskListUser

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/overdue/', TaskListOverdue.as_view(), name='task-list-overdue'),
    path('tasks/user/', TaskListUser.as_view(), name='task-list-user'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('users/tasks-count/', UserTaskCount.as_view(), name='user-task-count'),
]
