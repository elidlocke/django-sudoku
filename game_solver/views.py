from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Game
from .solver import SudokuGame
from .forms import NewSudokuForm

class IndexView(generic.ListView):
    template_name = 'game_solver/index.html'
    context_object_name = 'latest_games'

    def get_queryset(self):
        latest_games = Game.objects.filter(
            creation_date__lte=timezone.now()
        ).order_by('-creation_date')
        for game in latest_games:
            game.inputArray = [game.input[i:i+9].replace("0", " ") for i in range(0, len(game.input), 9)]
            game.outputArray = [game.output[i:i+9] for i in range(0, len(game.output), 9)]
        return latest_games

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game.inputArray = [game.input[i:i+9].replace("0", " ") for i in range(0, len(game.input), 9)]
    game.outputArray = [game.output[i:i+9] for i in range(0, len(game.output), 9)]
    return render(request, 'game_solver/detail.html', {'game': game})

def new(request):
    if request.method == 'POST':
        form = NewSudokuForm(request.POST)
        if form.is_valid():
            input = form.cleaned_data['input']
            play = SudokuGame(input)
            output = play.solveSudoku()
            game = Game.objects.create(input=input, output=output)
            #TODO: redirect should not be hardcoded to 1
            return HttpResponseRedirect('/game_solver/31/')
    else:
        form = NewSudokuForm()
    return render(request, 'game_solver/new.html', {'form': form})
