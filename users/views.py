from django.shortcuts import render
from .forms import UserForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
# Create your views here.


def register(request):
    registered = False
    user_form_errors = None

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid():

            print(user_form.cleaned_data)
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = True
            user.save()
            registered = True
            login(request, user)
            return HttpResponseRedirect(reverse("problems:home"))
        else:
            user_form_errors = user_form.non_field_errors
            print(user_form.errors)
    else: #if request.method == "POST":
        user_form = UserForm()
        # profile_form = UserProfileInfoForm()
    return render(request, 'users/register.html',
            {'registered':registered, 'user_form': user_form, 'user_errors': user_form_errors})
