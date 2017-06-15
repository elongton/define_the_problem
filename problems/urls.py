from django.conf.urls import url
from problems import views


app_name = 'problems'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^create/$', views.ProblemCreateView.as_view(), name='create'),
    url(r'^problem/(?P<pk>\d+)/$', views.ProblemDetailView.as_view(), name='problem_detail'),
]
