from django.urls import path
from jogos.core import views as v

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
]
