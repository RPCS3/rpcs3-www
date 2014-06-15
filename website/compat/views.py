from django.shortcuts import render

from website.compat.models import Title
from website.constants import *

def compat_index(request):
    stats = [
        len(Title.objects.filter(compatibility=C.COMPATIBILITY_NOTHING)),
        len(Title.objects.filter(compatibility=C.COMPATIBILITY_INTRO)),
        len(Title.objects.filter(compatibility=C.COMPATIBILITY_INGAME)),
        len(Title.objects.filter(compatibility=C.COMPATIBILITY_PLAYABLE)),
        len(Title.objects.filter(compatibility=C.COMPATIBILITY_PERFECT)),
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

def compat_list(request, char='', filter=None):
    return render(request, 'list.html')
