from unittest.mock import Mock
from django.test import Client, TestCase

from .forms import TeamForm
from .models import Team, Player


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
#Prueba de formato de score correcto
    def test_player_score_format(self):
        player1 = Player.objects.get(nombre='Jefferson FARFAN')
        player1.puntaje = 10500
        self.assertEqual(player1.puntaje_as_text(), '10,500')
#Prueba de que el pais existe en la base de datos
    def test_teams_exists(self):
        team1 = Team.objects.filter(pais='Perú')
        self.assertTrue(team1.exists())

        team2 = Team.objects.filter(pais='Alemania')
        self.assertTrue(team2.exists())
#Prueba de que jugador existe en la base de datos
    def test_players_exists(self):
        player1 = Player.objects.filter(nombre='Jefferson FARFAN')
        self.assertTrue(player1.exists())

        player2 = Player.objects.filter(nombre='Luis SUAREZ')
        self.assertTrue(player2.exists())
#Prueba el formulario
    def test_team_form_data_valid(self):
        form = TeamForm(data=self.team_data)
        self.assertTrue(form.is_valid())
#Prueba el formulario es incorrecto
    def test_team_form_data_invalid(self):
        form = TeamForm(data={})
        self.assertFalse(form.is_valid())
#Prueba que el puntaje sea el correcto
    def test_team_points(self):
        team_players = Player.objects.filter(id__in=self.team_data.values())
        score = sum([p.puntaje for p in team_players])
        response = self.client.post('/teams/', self.team_data)
        self.assertEqual(response.context.get('resultado'), score)
