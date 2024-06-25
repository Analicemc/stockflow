from rest_framework import serializers

from .models import Produto, Estoque

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Estoque
        fields = "__all__"

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Produto
        fields = "__all__"