from django.db import models


class PlayerManager(models.Manager):
    help = 'Creates a dict of player data'

    def __init__(self):


    def player_iterate(self):
        for row in self.data['rows']:
            print(dict(zip(self.data['headers'], row)))
            print(self.data)
