from django.shortcuts import render
from receitas.models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.all()

    dados = {
        'nome_das_receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')