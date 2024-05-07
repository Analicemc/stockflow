from django.db import models

class Estoque(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nro_lote   = models.CharField(max_length=100)
    qtde_ativa = models.IntegerField()