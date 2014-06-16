from django.conf.urls import patterns, url

urlpatterns = patterns('website.compat.views',
    url(r'^$', 'compat_index', name='compat-index'),
    url(r'^(?P<char>[a-zA-Z#])/$', 'compat_list', name='compat-list'),
    url(r'^(?P<title>[0-9a-zA-Z]{9,9})/$', 'compat_title', name='compat-title'),
)
