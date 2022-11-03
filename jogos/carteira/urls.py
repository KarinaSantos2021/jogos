from django.urls import path
from jogos.carteira import views

app_name = 'carteira'


urlpatterns = [
    path('', views.saldo_detail, name='saldo_detail'),
    path('depositar/', views.depositar, name='depositar'),
]
