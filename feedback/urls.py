from django.conf.urls import url
from feedback import views

app_name = 'feedback'


urlpatterns = [
    url(r'^feedback/create/$', views.FeedbackCreateView.as_view(), name='feedback_create'),
    url(r'^feedback/thanks/$', views.FeedbackThanksView.as_view(), name='feedback_thanks'),

]
