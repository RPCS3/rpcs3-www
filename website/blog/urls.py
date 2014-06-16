from django.conf.urls import patterns, url

urlpatterns = patterns('website.blog.views',
    url(r'^$', 'blog_pages', name='blog-index'),
    url(r'^page/(?P<num>[0-9]+)/$', 'blog_pages'),
    url(r'^tags/$', 'blog_pages', name='blog-entry'),
    url(r'^tags/(?P<slug>[-\w]+)/$', 'blog_pages', name='blog-entry'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'blog_entry', name='blog-entry'),
)
