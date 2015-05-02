from django.conf.urls import patterns, url

from SafeLevels import views

urlpatterns = patterns('',
    url(r'^$', views.welcomeSafeLevels, name='index'),
)
