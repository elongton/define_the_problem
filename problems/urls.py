from django.conf.urls import url
from problems import views

app_name = 'problems'

urlpatterns = [
    url(r'^$', views.index_topsix, name='home'),
    url(r'^create/(?P<pk>\d+)/(?P<pk2>\d+)/$', views.ProblemCreateView.as_view(), name='create'),
    url(r'^problem/(?P<pk>\d+)/$', views.ProblemDetailView.as_view(), name='problem_detail'),
    url(r'^browse/$', views.ProblemListView.as_view(), name='list'),
    url(r'^problem/(?P<pk>\d+)/addcomment/$', views.add_comment, name='createcomment'),
    url(r'^problem/(?P<pk>\d+)/addreply/$', views.add_reply_to_comment, name='createreply'),
    url(r'^problem/(?P<pk>\d+)/addreplyreply/$', views.add_reply_to_reply, name='createreplyreply'),
    url(r'^problem/(?P<pk>\d+)/likecomment/$', views.like_comment, name='likecomment'),
    url(r'^problem/(?P<pk>\d+)/likereply/$', views.like_reply, name='likereply'),
    url(r'^problem/(?P<pk>\d+)/likewhyrequest/$', views.like_why_request, name='likewhyrequest'),
    url(r'^problem/(?P<pk>\d+)/upvote/$', views.upvote_problem, name='detailupvote'),
    url(r'^problem/(?P<pk>\d+)/downvote/$', views.downvote_problem, name='detaildownvote'),
    url(r'^problem/(?P<pk>\d+)/addwhyrequest/$', views.add_why_request, name='addwhyrequest'),



    # url(r'^(?P<pk>\d+)/indexupvote/$',views.index_upvote, name='indexupvote'),
    # url(r'^(?P<pk>\d+)/indexdownvote/$',views.index_downvote, name='indexdownvote'),
    # url(r'^problem/(?P<pk>\d+)/(?P<ansc>\d+)/addwhy/$', views.add_why_to_problem, name='createwhy'),
    # url(r'^problem/(?P<pk>\d+)/listupvote/$', views.list_upvote, name='listupvote'),
    # url(r'^problem/(?P<pk>\d+)/listdownvote/$', views.list_downvote, name='listdownvote'),
    # url(r'^problem/(?P<pk>\d+)/(?P<type>\d+)/requestwhy/$', views.request_why, name='requestwhy'),
    # url(r'^problem/(?P<pk>\d+)/whyupvote/$', views.upvote_why, name='whyupvote'),
    # url(r'^problem/(?P<pk>\d+)/whydownvote/$', views.downvote_why, name='whydownvote'),

]
