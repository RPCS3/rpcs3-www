from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Public
    url(r'^$', 'website.home.views.home', name='home'),
    url(r'^contact/$', 'website.home.views.contact', name='contact'),
    url(r'^compat/', include('website.compat.urls')),
    url(r'^blog/', include('website.blog.urls')),

    # Administration
    url(r'^admin/', include(admin.site.urls)),
)
