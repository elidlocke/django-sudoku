from django.shortcuts import render, get_object_or_404

from .models import Game

def index(request):
    latest_games = Game.objects.order_by('creation_date')
    context = { 'latest_games': latest_games }
    return render(request, 'game_solver/index.html', context)

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game_solver/detail.html', {'game': game})
