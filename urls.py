from django.conf.urls.defaults import *
from geofinder import view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
			(r'^search/$',view.searchform),
			(r'^search/(\w*)/(\w*)/$',view.search),
			(r'^search/json/(\w*)/(\w*)/$',view.searchjson),
    # Example:
    # (r'^geofinder/', include('geofinder.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
