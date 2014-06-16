from django.conf.urls import patterns, url

urlpatterns = patterns('website.blog.views',
    url(r'^$', 'blog_index', name='blog-index'),
)
