from django.contrib import admin
from .models import Problem, Comment
# Register your models here.

admin.site.register(Problem, Comment)
