from django.db import models
from datetime import datetime

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "Users"

class questions(models.Model):
    question = models.CharField(max_length=250)
    #body = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "Questions"

class answers(models.Model):
    answer = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    def __str__(self):
        return self.answer
    class Meta:
        verbose_name_plural = "Answers"

class lobbies(models.Model):
    name = models.CharField(max_length=200)
    players = models.CharField(max_length=200)
    lobpass = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    game = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Trivia Lobbies"


class teams(models.Model):
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.pais

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"


class players(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.ForeignKey('teams', on_delete=models.CASCADE)
    puntaje = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"
