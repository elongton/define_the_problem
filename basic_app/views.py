from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context


class SchoolListView(ListView):
    #ListView creates the context dictionary for us!
    #It takes the model we call, lowercases it, and then adds "_list"
    model = models.School
    #however, you can use a class object attribute to define a different context variable
    #context_object_name = 'schools'

class SchoolDetailView(DetailView):
    #DetailView creates the context dictionary for us and just lowercases the model name.
    context_object_name = 'school_detail'  #hence changing the context_object_name
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('principal', 'name',)
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
    #reverse_lazy is only called if there is a success
