from django.core.management.base import BaseCommand, CommandError

from datetime import datetime
from website.compat.models import Game

class Command(BaseCommand):
    args = "<file>"
    help = "Deletes the compatibility database and restarts it from the given CSV backup."

    def handle(self, *args, **options):
        f = open(args[0], 'r')

        for line in f.readlines():
            # Manually parsing the CSV file, don't try this at home!
            fields = line[:-1].split(",")
            for i in xrange(len(fields)):
                if fields[i].startswith('"') and fields[i].endswith('"'):
                    fields[i] = fields[i][1:-1]
                if i == 5:
                    try:
                        fields[i] = datetime.strptime(fields[i], "%Y-%m-%d")
                    except:
                        # If there is no specific release date, choose PS3's release date
                        fields[i] = datetime.strptime("2006-06-11", "%Y-%m-%d")

            # Create and save the object
            game = Game(
                titleid=fields[0], name=fields[1], publisher=fields[2], developer=fields[3],
                genre=fields[4], release=fields[5], firmware=fields[6], compatibility=fields[7],
            )
            game.save()

        f.close()
