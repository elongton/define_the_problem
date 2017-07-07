from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.generic import (View, TemplateView,
                                  CreateView, DetailView,
                                  ListView)
from feedback.forms import FeedbackForm
from . import models


class FeedbackThanksView(TemplateView):
    template_name = 'feedback/feedback_thanks.html'

class FeedbackCreateView(CreateView):
    model = models.Feedback
    fields = ('text',)
    template_name = 'feedback/feedback_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
