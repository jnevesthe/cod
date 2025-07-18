from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import InfoListView, Index, Sobre, Servicos, Contato, Termos, Privacidade
from django.http import FileResponse
import os

urlpatterns = [
    path('info/', InfoListView.as_view(), name='info'),
    path('', Index.as_view(), name='index'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('services/', Servicos, name='servicos'),
    path('contato/', Contato.as_view(), name='contato'),

    # Novas páginas obrigatórias para AdSense
    path('termos/', Termos.as_view(), name='termos'),
    path('privacidade/', Privacidade.as_view(), name='privacidade'),

    # Arquivo ads.txt
    path("ads.txt", lambda request: FileResponse(open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "ads.txt"), "rb"
    ))),
]

# Arquivos estáticos (modo desenvolvimento)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
