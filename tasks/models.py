from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50,choices=[('pending','Pending'),('completed','Completed')])
    due_date = models.DateField(null=True,blank=True)
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='tasks')

    def __str__(self):
        return self.title
    
   
