from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "Users"

class Question(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "Questions"

class Answer(models.Model):
    answer = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    def __str__(self):
        return self.answer
    class Meta:
        verbose_name_plural = "Answers"

class Lobby(models.Model):
    name = models.CharField(max_length=200)
    players = models.TextField()
    lobpass = models.CharField(max_length=200)
    ltype = models.CharField(max_length=200)
    game = models.CharField(max_length=200)
    administrator = models.CharField(max_length=200)
    gamemode = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def players_as_list(self):
        return self.players.split(',')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Trivia Lobbies"


class Team(models.Model):
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.pais

    class Meta:
        db_table = 'mundialitisapps_teams'
        verbose_name = "Team"
        verbose_name_plural = "Teams"


class Player(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.ForeignKey('Team', on_delete=models.CASCADE)
    puntaje = models.IntegerField()

    def __str__(self):
        return self.nombre

    def puntaje_as_text(self):
        return '{:,}'.format(self.puntaje)

    class Meta:
        db_table = 'mundialitisapps_players'
        verbose_name = "Player"
        verbose_name_plural = "Players"
