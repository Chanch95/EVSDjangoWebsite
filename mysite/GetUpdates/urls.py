from django.conf.urls import patterns, url

from GetUpdates import views

urlpatterns = patterns('',
    url(r'^$', views.welcomeGetUpdates, name='index'),
)
