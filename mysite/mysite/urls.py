from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^AirCheck/', include('AirCheck.urls')),
    url(r'^AirCheck/Poll/', include('Poll.urls')),
    url(r'^AirCheck/About/', include('About.urls')),
    url(r'^AirCheck/SafeLevels/', include('SafeLevels.urls')),
    url(r'^AirCheck/Tool/', include('Tool.urls')),
    url(r'^AirCheck/Measures/', include('Measures.urls')),
    url(r'^AirCheck/Team/', include('Team.urls')),
    url(r'^AirCheck/GetUpdates/', include('GetUpdates.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
