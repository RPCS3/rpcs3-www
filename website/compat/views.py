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

    # TODO: Rewrite this with more Django style
    results = []
    for i in range(len(stats))[::-1]:
        results.append({
            'category' : C.COMPATIBILITY[i+1][1],                                 # e.g. 'Playable'
            'string' : '%.2f' % (100.0 * stats[i] / total if total else 0),       # e.g. '12.34'
            'int' : 100 * stats[i] / total if total else 0,                       # e.g.  12
            'color' : ['#555555', '#D9534F', '#F0AD4E', '#5CB85C', '#428BCA'][i], # e.g. '#5CB85C'
        })

    objects = {
        'results' : results,
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
