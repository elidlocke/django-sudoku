from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Game
from .solver import SudokuGame

class IndexView(generic.ListView):
    template_name = 'game_solver/index.html'
    context_object_name = 'latest_games'

    def get_queryset(self):
        latest_games = Game.objects.filter(
            creation_date__lte=timezone.now()
        ).order_by('-creation_date')
        return latest_games

class DetailView(generic.DetailView):
    model = Game
    template_name = 'game_solver/detail.html'

def new(request):
    if request.method == 'POST':
        input = request.POST['input']
        play = SudokuGame(input)
        output = play.solveSudoku()
        game = Game.objects.create(input=input, output=output)
    return render(request, 'game_solver/new.html')
