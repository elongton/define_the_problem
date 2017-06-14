from django.contrib import admin
<<<<<<< HEAD
from problems.models import Problem, Comment
=======
from .models import Problem, Comment
>>>>>>> 99d74667a5f705f11392ac5f4cd489ac965a0b48
# Register your models here.

admin.site.register(Problem)
admin.site.register(Comment)
