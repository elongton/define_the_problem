from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View, TemplateView,
                                  CreateView, DetailView,
                                  ListView)
from problems.forms import ProblemForm, CommentForm, ReplyForm
from . import models



#######################
# FUNCTION BASED VIEWS
#######################

@login_required
def like_comment(request,pk):
    comment = get_object_or_404(models.Comment,pk=pk)
    comment.like()
    return redirect('problems:problem_detail',pk=comment.problem.pk)

@login_required
def like_reply(request,pk):
    reply = get_object_or_404(models.Reply,pk=pk)
    reply.like()
    return redirect('problems:problem_detail',pk=comment.problem.pk)

@login_required
def add_reply_to_reply(request,pk):
    base_reply = get_object_or_404(models.Reply,pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = base_reply.comment
            reply.author = request.user
            reply.save()
            return redirect('problems:problem_detail',pk=reply.comment.problem.pk)
    else:
        form = ReplyForm()
    return render(request,'problems/reply_add.html',{'form':form, 'reply':base_reply})

@login_required
def add_reply_to_comment(request,pk):
    comment = get_object_or_404(models.Comment,pk=pk)
    print(comment.pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.author = request.user
            reply.save()
            return redirect('problems:problem_detail',pk=comment.problem.pk)
    else:
        form = ReplyForm()
    return render(request,'problems/reply_add.html',{'form':form, 'comment':comment})

@login_required
def add_comment_to_problem(request,pk):
    problem = get_object_or_404(models.Problem,pk=pk)
    print(problem.pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.problem = problem
            comment.author = request.user
            comment.save()
            return redirect('problems:problem_detail',pk=problem.pk)
    else:
        form = CommentForm()
    return render(request,'problems/comment_add.html',{'form':form, 'problem':problem})

#######################
# CLASS BASED VIEWS
#######################
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
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ProblemCreateView, self).form_valid(form)

class ProblemDetailView(DetailView):
    model = models.Problem
    context_object_name = 'problem'
    template_name = 'problems/problem_detail.html'

class ProblemListView(ListView):
    model = models.Problem
    context_object_name = 'problems'
    template_name = 'problems/problem_list.html'
