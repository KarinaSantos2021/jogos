from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Dezena(models.Model):
    dezena = models.IntegerField()

class Bicho(models.Model):
    nome = models.CharField(max_length=200)
    numero = models.IntegerField()
    dezenas = models.ManyToManyField(Dezena)

class Numero(models.Model):
    numero = models.IntegerField()

class ApostaDoJogoDoBicho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numeros = models.ManyToManyField(Numero)
    data = models.DateTimeField(default=datetime.now)

