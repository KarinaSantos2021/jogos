from django.contrib import admin

from .models import Saldo


@admin.register(Saldo)
class SaldoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'saldo')
    search_fields = ('usuario', 'saldo')
