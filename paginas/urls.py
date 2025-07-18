from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import InfoListView, Index, Sobre, Servicos, Contato
from django.http import FileResponse
import os

urlpatterns = [
    path('info/', InfoListView.as_view(), name='info'),
    path('', Index.as_view(), name='index'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('services/', Servicos, name='servicos'),
    path('contato/', Contato.as_view(), name='contato'),

    # Rota para o ads.txt
    path("ads.txt", lambda request: FileResponse(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "ads.txt"), "rb"))),
]

# (opcional) se estiver servindo arquivos estáticos localmente em DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
