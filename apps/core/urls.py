from django.urls import path, include
from apps.core.views import index

urlpatterns = [
    path("", index, name='index'),
]