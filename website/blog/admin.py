from django.contrib import admin
from website.blog.models import Article, Tag

admin.site.register(Article)
admin.site.register(Tag)
