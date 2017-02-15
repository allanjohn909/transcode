from django.conf.urls import url
from transcode import views

urlpatterns = [
        url(r'^$', views.HomePageView.as_view()),
        url(r'^start/$', views.start, name='start'),
        url(r'^start/list/$', views.list, name='list'),
        
        
    ]