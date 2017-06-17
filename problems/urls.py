from django.conf.urls import url
from problems import views


app_name = 'problems'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^create/$', views.ProblemCreateView.as_view(), name='create'),
    url(r'^problem/(?P<pk>\d+)/$', views.ProblemDetailView.as_view(), name='problem_detail'),
    url(r'^browse/$', views.ProblemListView.as_view(), name='list'),
    url(r'^problem/(?P<pk>\d+)/addcomment/$', views.add_comment_to_problem, name='createcomment'),
    url(r'^problem/(?P<pk>\d+)/addreply/$', views.add_reply_to_comment, name='createreply'),
    url(r'^problem/(?P<pk>\d+)/addreplyreply/$', views.add_reply_to_reply, name='createreplyreply'),
    url(r'^problem/(?P<pk>\d+)/likecomment/$', views.like_comment, name='likecomment'),
]
