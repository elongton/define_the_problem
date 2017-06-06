from django.shortcuts import render
from users_app.forms import UserForm


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('patron_password_app:search'))
    else:
        return render(request,'index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def next_screen(request):
    return HttpResponseRedirect(reverse('patron_password_app:search'))


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
            user.is_active = False
            user.save()
            # user.set_password(user.password)
            registered = True
            return index(request)
        else:
            user_form_errors = user_form.non_field_errors
            print(user_form.errors)
    else: #if request.method == "POST":
        user_form = UserForm()
        # profile_form = UserProfileInfoForm()
    return render(request, 'users_app/register.html',
            {'registered':registered, 'user_form': user_form, 'user_errors': user_form_errors})





def user_login(request): #don't call this "login" because it doubles the imported function
    # if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) #always type in parameters

        if user:
            if user.is_active:
                login(request, user)
                return next_screen(request)
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("<h1>Invalid login details supplied!</h1>")

    # else:
    #     return render(request, 'basic_app/login.html', {})
