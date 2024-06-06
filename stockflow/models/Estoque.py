from django.db import models

class Estoque(models.Model):
    produto_id   = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nro_lote     = models.CharField(max_length=100)
    qtde_inicial = models.IntegerField() 
    qtde_ativa   = models.IntegerField()

@classmethod
def criar_estoque(cls, produto_id, qtde_inicial, nro_lote):
    try:
        estoque = cls(
            produto_id=produto_id,
            qtde_ativa=qtde_inicial,
            nro_lote=nro_lote
        )
        estoque.save()
        return estoque
    except Exception as e:
        print(f"Erro ao criar estoque: {e}")
        return None
    
def incrementar_estoque(self, quantidade):
    try:
        self.qtde_ativa += quantidade
        self.save()
    except Exception as e:
        print(f"Erro ao incrementar estoque: {e}")

def decrementar_estoque(self, quantidade):
    try:
        if quantidade > self.qtde_ativa:
            print("Erro: quantidade a decrementar maior que a quantidade ativa em estoque.")
            return
        self.qtde_ativa -= quantidade
        self.save()
    except Exception as e:
        print(f"Erro ao decrementar estoque: {e}")