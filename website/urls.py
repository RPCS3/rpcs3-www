from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Public
    url(r'^$', 'website.home.views.home', name='home'),

    # Administration
    url(r'^admin/', include(admin.site.urls)),
)
