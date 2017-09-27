from django.db import models

# Create your models here.


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    minutes = models.DecimalField(max_digits=3, decimal_places=1)
    points = models.DecimalField(max_digits=3, decimal_places=1)
    fgm = models.DecimalField(max_digits=3, decimal_places=1)
    fga = models.DecimalField(max_digits=3, decimal_places=1)
    threes_m = models.DecimalField(max_digits=3, decimal_places=1)
    threes_a = models.DecimalField(max_digits=3, decimal_places=1)
    rebounds = models.DecimalField(max_digits=3, decimal_places=1)
    assists = models.DecimalField(max_digits=3, decimal_places=1)
    steals = models.DecimalField(max_digits=3, decimal_places=1)
    blocks = models.DecimalField(max_digits=3, decimal_places=1)
    turnovers = models.DecimalField(max_digits=3, decimal_places=1)
    team = models.CharField(max_length=3)

    def __str__(self):
        name = [self.first_name, self.last_name]
        return ' '.join(name)
