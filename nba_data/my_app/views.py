from django.shortcuts import render

# Create your views here.


def player_list(request):
    return render(request, 'player_list.html', {})
