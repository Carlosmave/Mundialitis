from unittest.mock import Mock
from django.test import Client, TestCase

from .forms import TeamForm
from .models import teams, players


class TeamsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.team_data = {
            'arquero': 1,
            'defensa1': 2,
            'defensa2': 3,
            'defensa3': 4,
            'defensa4': 5,
            'centro1': 6,
            'centro2': 7,
            'centro3': 8,
            'delantero1': 9,
            'delantero2': 10,
            'delantero3': 11,
        }

    def test_teams_exists(self):
        team1 = teams.objects.filter(pais='Perú')
        self.assertTrue(team1.exists())

        team2 = teams.objects.filter(pais='Alemania')
        self.assertTrue(team2.exists())

    def test_players_exists(self):
        player1 = players.objects.filter(nombre='Jefferson FARFAN')
        self.assertTrue(player1.exists())

        player2 = players.objects.filter(nombre='Luis SUAREZ')
        self.assertTrue(player2.exists())

    def test_team_form_data(self):
        form = TeamForm(data=self.team_data)
        self.assertTrue(form.is_valid())

    def test_team_points(self):
        team_players = players.objects.filter(id__in=self.team_data.values())
        score = sum([p.puntaje for p in team_players])
        response = self.client.post('/teams/', self.team_data)
        self.assertEqual(response.context.get('resultado'), score)
