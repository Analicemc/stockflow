from django.contrib import admin
from .models.Produto import Produto
from .models.Estoque import Estoque

admin.site.register(Produto)
admin.site.register(Estoque)