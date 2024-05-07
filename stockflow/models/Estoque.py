from django.db import models

class Estoque(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
