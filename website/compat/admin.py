from django.contrib import admin
from website.compat.models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ('titleid', 'name', 'compatibility')

admin.site.register(Game, GameAdmin)
