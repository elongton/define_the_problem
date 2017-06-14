from django.shortcuts import render
from django.views.generic import (View, TemplateView,)

# Create your views here.
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'
