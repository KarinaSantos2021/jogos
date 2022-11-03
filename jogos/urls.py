from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('jogos.core.urls', namespace='core')),
    path('accounts/', include('jogos.accounts.urls')),
    path('carteira/', include('jogos.carteira.urls', namespace='carteira')),
    path('jogo_do_bicho/', include('jogos.jogo_do_bicho.urls', namespace='bicho')),
    path('admin/', admin.site.urls),
]
