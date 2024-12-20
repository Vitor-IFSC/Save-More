from django.contrib import admin
from .models import Compra, Instituicao

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_item', 'preco', 'quantidade', 'instituicao')  # Campos reais do modelo
    search_fields = ('nome_item',)  # Corrija aqui também
    list_filter = ('instituicao',)

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_instituicao')
    search_fields = ('nome_instituicao',)
