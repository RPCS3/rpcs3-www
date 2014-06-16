from django.db import models

from website.constants import *

class Game(models.Model):
    # Static
    titleid = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    developer = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    release = models.DateField()
    firmware = models.CharField(max_length=8)

    # Dynamic
    compatibility = models.SmallIntegerField(choices=C.COMPATIBILITY)

    # Methods
    def __unicode__(self):
        return self.name

    def get_region(self):
        if len(self.titleid):
            return 'Unknown!'

        # Regions
        if self.titleid[2] == 'A': return 'Asia'
        if self.titleid[2] == 'E': return 'Europe'
        if self.titleid[2] == 'H': return 'Southeast Asia'
        if self.titleid[2] == 'K': return 'Hong Kong'
        if self.titleid[2] == 'I': return 'Internal (Sony)'
        if self.titleid[2] == 'J': return 'Japan'
        if self.titleid[2] == 'U': return 'USA'
        if self.titleid[2] == 'X': return 'Firmware/SDK Sample'
        return 'Unknown!'