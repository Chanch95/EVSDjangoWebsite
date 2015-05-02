from django.conf.urls import patterns, url

from Tool import views

urlpatterns = patterns('',
    url(r'^$', views.welcomeTool, name='index'),
    url(r'^$', views.resultPage, name='index'),
)
