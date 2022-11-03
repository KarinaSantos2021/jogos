from django.contrib.auth.models import User
from django.db import models

class Saldo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saldos")
    saldo = models.FloatField()
