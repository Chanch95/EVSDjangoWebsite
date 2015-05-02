from django.conf.urls import patterns, url

from Team import views

urlpatterns = patterns('',
    url(r'^$', views.welcomeTeam, name='index'),
)
