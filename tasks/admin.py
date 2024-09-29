from django.contrib import admin

# Register your models here.
from .models import Profile, Category, Task  # Import the models

# Register your models to make them visible in the admin panel
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Task)
