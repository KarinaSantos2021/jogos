from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Bola(models.Model):
    numero = models.IntegerField()


class LoteriaSorteio(models.Model):
    data = models.DateTimeField(default=datetime.now)
    bolas_sorteadas = models.ManyToManyField(Bola)

class ApostaLoteria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numeros_do_bilhete = models.ManyToManyField(Bola)
    data = models.DateTimeField(default=datetime.now)
