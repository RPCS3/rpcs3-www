from django.http import Http404
from django.shortcuts import render

from website.compat.models import Game
from website.constants import *


def compat_index(request):
    stats = [
        len(Game.objects.filter(compatibility=C.COMPATIBILITY_NOTHING)),
        len(Game.objects.filter(compatibility=C.COMPATIBILITY_INTRO)),
        len(Game.objects.filter(compatibility=C.COMPATIBILITY_INGAME)),
        len(Game.objects.filter(compatibility=C.COMPATIBILITY_PLAYABLE)),
        len(Game.objects.filter(compatibility=C.COMPATIBILITY_PERFECT)),
    ]
    total = sum(stats)
    strResults = map(lambda x: '%.2f' % (100.0*x/total if total else 0), stats)
    intResults = map(lambda x: 100*x/total if total else 0, stats)

    objects = {
        'strResults' : strResults,
        'intResults' : intResults,
        'chars' : '#ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    }
    return render(request, 'index.html', objects)


def compat_list(request, char):
    gameList = Game.objects.filter(name__startswith=char)
    objects = {
        'gameList' : gameList,
        'chars' : '#ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    }
    return render(request, 'list.html', objects)


def compat_title(request, title):
    print title
    try:
        game = Game.objects.get(titleid=title)
    except Game.DoesNotExist:
        raise Http404

    return render(request, 'title.html', {'game' : game})
