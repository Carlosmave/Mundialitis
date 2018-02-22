from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    money = models.IntegerField()
    def __str__(self):
        return self.username

class Question(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    def __str__(self):
        return self.answer

class Partido(models.Model):
    equipo_a = models.TextField()
    equipo_b = models.TextField()

class Polla(models.Model):
    estado = models.BooleanField(default=False)

class PollaPartido(models.Model):
    id_partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    ganador = models.TextField()
    
class PollaApuesta(models.Model):
    polla_partido = models.ForeignKey(PollaPartido, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apuesta = models.TextField()

class PollaPuntaje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)
    
class Lobby(models.Model):
    name = models.CharField(max_length=200)
    players = models.TextField()
    lobpass = models.CharField(max_length=200)
    ltype = models.CharField(max_length=200)
    game = models.CharField(max_length=200)
    administrator = models.CharField(max_length=200)
    gamemode = models.CharField(max_length=200)
    lstatus = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    moneybet =  models.IntegerField()
    playerscores =  models.TextField()
    winner = models.CharField(max_length=200)
    def players_as_list(self):
        return self.players.split(',')
    def playerscores_as_list(self):
        return self.playerscores.split(',')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Trivia Lobbies"

class Partido(models.Model):
    equipo_a = models.TextField()
    equipo_b = models.TextField()

class Polla(models.Model):
    estado = models.BooleanField(default=False)

class PollaPartido(models.Model):
    id_partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    ganador = models.TextField()

class PollaApuesta(models.Model):
    polla_partido = models.ForeignKey(PollaPartido, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apuesta = models.TextField()

class PollaPuntaje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)
