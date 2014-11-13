from django.conf.urls import patterns, include, url

from views import showHello
from admin.views import addName
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    

    url(r'^$', showHello),
    url(r'^admin/$', addName),

    # Examples:
    # url(r'^$', 'Practice.views.home', name='home'),
    # url(r'^Practice/', include('Practice.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
