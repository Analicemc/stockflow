from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Estoque, Produto

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import Response: Any

class EstoqueListView(ListView):
    model = Estoque
    template_name = 'estoque_list.html'
    context_object_name = 'estoques'

def estoque_detail(request, pk):
    estoque = get_object_or_404(Estoque, pk=pk)
    return render(request, 'estoque_detail.html', {'estoque': estoque})

