from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Game
from .solver import SudokuGame
#from .forms import NewSudokuForm

def index(request):
    latest_games = Game.objects.order_by('creation_date')
    context = { 'latest_games': latest_games }
    return render(request, 'game_solver/index.html', context)

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game_solver/detail.html', {'game': game})

def new(request):
    if request.method == 'POST':
        input = request.POST['input']
        play = SudokuGame(input)
        output = play.solveSudoku()
        game = Game.objects.create(input=input, output=output)
    return render(request, 'game_solver/new.html')