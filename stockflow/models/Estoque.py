from django.db import models

class Estoque(models.Model):
    produto_id   = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nro_lote     = models.CharField(max_length=100)
    qtde_inicial = models.IntegerField() 
    qtde_ativa   = models.IntegerField()

    def criar_estoque(self, produto_id, qtde_inicial, nro_lote):
        estoque = Estoque()
        estoque.produto_id = produto_id
        estoque.qtde_ativa = qtde_inicial
        estoque.nro_lote = nro_lote
        estoque.save()

    """def retirar_estoque(self, nro_lote, qtde):
        Estoque."""