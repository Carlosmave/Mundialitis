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

<<<<<<< HEAD
class Partido(models.Model):
    equipo_a = models.TextField()
    equipo_b = models.TextField()

class Polla(models.Model):
    id_partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    ganador = models.TextField()
    
class PollaApuesta(models.Model):
    id_polla = models.ForeignKey(Polla, on_delete=models.CASCADE)
    id_user = models.ForeignKey(users, on_delete=models.CASCADE)
    apuesta = models.TextField()
=======
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
>>>>>>> 06d0afcc691588639511583cd98163374526b61c
