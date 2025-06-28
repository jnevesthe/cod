from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import InfoListView, Index, Sobre, Servicos, Contato 

from . import views


urlpatterns=[

    path('info/', InfoListView.as_view(), name='info'),
    path('', Index.as_view(), name='index'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('services/', views.Servicos, name='servicos'),
    path('contato/', Contato.as_view(), name='contato'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)