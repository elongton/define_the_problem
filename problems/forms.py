from django import forms
from problems.models import Problem, Comment, Reply


class ProblemForm(forms.ModelForm):
    class Meta():
        model = Problem
        fields = ('text',)


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('text',)

class ReplyForm(forms.ModelForm):
    class Meta():
        model = Reply
        fields = ('text',)