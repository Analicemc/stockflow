from django.db import models

class Produto(models.Model):
    nome = models.CharField()
    
    def __str__(self):
        return self.nome
