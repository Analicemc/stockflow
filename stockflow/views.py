from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Estoque
from .serializers import EstoqueSerializer

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class EstoqueListView(ListView):
    model = Estoque
    template_name = 'estoque_list.html'
    context_object_name = 'estoques'

def estoque_detail(request, pk):
    estoque = get_object_or_404(Estoque, pk=pk)
    return render(request, 'estoque_detail.html', {'estoque': estoque})


# API REST
@api_view(['GET'])
def get_stocks(request):
    if request.method == 'GET':
        estoques   = Estoque.objects.all()
        serializer = EstoqueSerializer(estoques, many = True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_stock(request, pk):
    if request.method == 'GET':
        try:
            estoque = Estoque.objects.get(pk=pk)
            serializer = EstoqueSerializer(estoque)
            return Response(serializer.data)
        except Estoque.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_stock(request):
    if request.method == 'POST':
        serializer = EstoqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_stock(request, pk):
    try:
        estoque = Estoque.objects.get(pk=pk)
    except Estoque.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        estoque.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['PUT'])
def update_stock(request, pk):
    try:
        estoque = Estoque.objects.get(pk=pk)
    except Estoque.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = EstoqueSerializer(estoque, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)