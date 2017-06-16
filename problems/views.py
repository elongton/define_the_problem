from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import (View, TemplateView,
                                  CreateView, DetailView)
from . import models

class IndexView(TemplateView):
    template_name = 'sitewide/index.html'

class ProblemCreateView(CreateView):
    model = models.Problem
    fields = ('text',)
    template_name = 'problems/problem_add.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(ProblemCreateView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("users:login"))

class ProblemDetailView(DetailView):
    model = models.Problem
    context_object_name = 'problem'
    template_name = 'problems/problem_detail.html'
