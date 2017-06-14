from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views as userviews

app_name = 'users'


urlpatterns = [
    # url('^', include('django.contrib.auth.urls')),
    url('^login/$',auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    url('^logout/$',auth_views.LogoutView.as_view(), name="logout"),
    # url('^passwordreset/$',auth_views.PasswordResetView.as_view(template_name='users/passwordreset.html'), name="password_reset"),
    url(r'^register/$', userviews.register, name='register'),
]
