from django.conf.urls import patterns, url

urlpatterns = patterns('website.compat.views',
    url(r'^$', 'compat_index', name='compat-index'),
    url(r'^(?:(?P<char>[A-Z#])/)?(?:filter/(?P<filter>[12345])/)?$', 'compat_list', name='compat-list'),
)
