from django.urls import path, include
from apps.core.views import index
from apps.map.views import mapa_view
from . import views

urlpatterns = [
    path('mapa/', views.mapa_view, name='mapa_view'),
    path('fazer_doacao/', views.fazer_doacao, name='fazer_doacao'),
]
