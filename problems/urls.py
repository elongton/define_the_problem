from django.conf.urls import url
from problems import views


app_name = 'problems'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
]
