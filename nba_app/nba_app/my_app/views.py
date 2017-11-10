from django.shortcuts import render
from .models import Player

# Create your views here.


def player_list(request):
    players = Player.objects.order_by('pts')
    return render(request, 'player_list.html', {'players': players})
