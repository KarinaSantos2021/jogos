from django.contrib import admin

from .models import ApostaLoteria, LoteriaSorteio, Bola


@admin.register(ApostaLoteria)
class ApostaLoteriaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data')
    search_fields = ('usuario', 'data')

@admin.register(LoteriaSorteio)
class LoteriaSorteioAdmin(admin.ModelAdmin):
    list_display = ('data',)
    search_fields = ('data',)

@admin.register(Bola)
class BolaAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    search_fields = ('numero',)
