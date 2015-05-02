from django.conf.urls import patterns, url

from Measures import views

urlpatterns = patterns('',
    url(r'^$', views.welcomeMeasures, name='index'),
)
