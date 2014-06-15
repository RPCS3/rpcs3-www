from django.db import models

from website.constants import *

class Title(models.Model):
    # Static
    titleid = models.CharField(max_length=9)
    name = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    developer = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    release = models.DateField()
    firmware = models.CharField(max_length=8)

    # Dynamic
    compatibility = models.SmallIntegerField(choices=C.COMPATIBILITY)
