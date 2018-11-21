import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Game
from django.urls import reverse

# Create your tests here.
class GameModelTests(TestCase):
    def test_str_returns_input(self):
        aGame = Game("012345678")
        self.assertEqual(aGame.input, str(aGame))

def create_game(input, output, date=None):
    if date == None:
        date = timezone.now()
    return Game.objects.create(input=input, output=output, creation_date=date)

class GameIndexViewTests(TestCase):
    def test_no_games(self):
        response = self.client.get(reverse('game_solver:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_games'], [])

    def test_past_questions(self):
        create_game("in", "out", timezone.now() - datetime.timedelta(8))
        response = self.client.get(reverse('game_solver:index'))
        self.assertQuerysetEqual(
            response.context['latest_games'],
            ['<Game: in>']
        )

    def test_future_questions(self):
        game = create_game("in", "out", (timezone.now() + datetime.timedelta(days=50)))
        response = self.client.get(reverse('game_solver:index'))
        print(response.context['latest_games'])
        self.assertQuerysetEqual(response.context['latest_games'], [])
