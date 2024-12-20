from django.db import models
    
class Instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=255, verbose_name='Nome da Instituição')
    endereco = models.CharField(max_length=255, verbose_name='Endereço', blank=True, null=True)

    def __str__(self):
        return self.nome_instituicao

class Compra(models.Model):
    nome_item = models.CharField('Nome do Item', max_length=255)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    endereco = models.CharField('Endereço', max_length=255)
    quantidade = models.IntegerField('Quantidade')
    numero_contato = models.CharField('Número para Contato', max_length=20)
    foto_item = models.ImageField('Foto do Item', upload_to='fotos_itens', blank=True, null=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name='Instituição')

    def __str__(self):
        return self.nome_item

