from django import forms
from problems.models import Problem, Comment


class ProblemForm(forms.ModelForm):

    class Meta():
        model = Problem
        fields = ('text')
