from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  CreateView, DetailView)
from . import models

class IndexView(TemplateView):
    template_name = 'sitewide/index.html'

class ProblemCreateView(CreateView):
    model = models.Problem
    fields = ('text',)
    template_name = 'problems/problem_add.html'

class ProblemDetailView(DetailView):
    model = models.Problem
    context_object_name = 'problem'
    template_name = 'problems/problem_detail.html'
