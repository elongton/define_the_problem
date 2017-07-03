from django.contrib import admin
from problems.models import Problem, Comment, Reply, WhyRequest
# Register your models here.

admin.site.register(Problem)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(WhyRequest)
# admin.site.register(Why)
