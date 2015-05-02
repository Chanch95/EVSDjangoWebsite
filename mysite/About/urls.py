from django.conf.urls import patterns, url

from About import views

urlpatterns = patterns('',
    url(r'^$', views.welcomeAbout, name='welcomeAbout'),
)
