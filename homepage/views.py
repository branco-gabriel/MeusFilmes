from django.shortcuts import render
from .models import Filme

def index(request):
    filmes = Filme.objects.order_by('id').filter()
    return render(request, 'homepage/index.html', {'filmes': filmes})
