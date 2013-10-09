from django.conf.urls import patterns, include, url
from conference.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scipy2012.views.home', name='home'),
    # url(r'^scipy2012/', include('scipy2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^keynote/', keynote),    
    url(r'^tutorials/', tutorials),
    url(r'^talks/', talks),
    url(r'^sponsors/', sponsors),
    url(r'^details/(\d+)/$', details),
)
