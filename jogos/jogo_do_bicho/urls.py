from django.urls import path
from jogos.jogo_do_bicho import views

app_name = 'jogo_do_bicho'


urlpatterns = [
    path('', views.aposta_detail, name='aposta_detail'),
    path('apostar/', views.apostar, name='apostar'),
]
