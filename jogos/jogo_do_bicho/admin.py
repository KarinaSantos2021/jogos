from django.contrib import admin

from .models import ApostaDoJogoDoBicho, Bicho, Numero, Dezena


@admin.register(ApostaDoJogoDoBicho)
class ApostaDoJogoDoBichoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data')
    search_fields = ('usuario', 'data')

@admin.register(Numero)
class NumeroAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    search_fields = ('numero',)

@admin.register(Bicho)
class BichoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero')

    search_fields = ('nome', 'numero')
