from django.db import models

import markdown
from django.template.defaultfilters import slugify


class Tag(models.Model):
    tag = models.CharField(max_length=31)
    def __unicode__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()
    visible = models.BooleanField()
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.id: # Newly created object, so set slug
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_formatted_content(self):
        return markdown.markdown(self.content)
