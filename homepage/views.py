from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme
from django.http import Http404
from .forms import PostForm


def index(request):
    filmes = Filme.objects.order_by('id').filter()
    return render(request, 'homepage/index.html', {'filmes': filmes})


def ver_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if not filme.mostrar:
        raise Http404
    else:
        return render(request, 'homepage/ver_filme.html', {'filme': filme})


def adicionar(request):
    form = PostForm()

    if(request.method == 'POST'):
        form = PostForm(request.POST)

        if(form.is_valid()):
            post_filme = form.cleaned_data['filme']
            post_categoria = form.cleaned_data['categoria']
            post_resenha = form.cleaned_data['resenha']

            new_post = Filme(filme=post_filme, categoria=post_categoria, resenha=post_resenha)
            new_post.save()

            return redirect('index')

    elif(request.method == 'GET'):
        return render(request, 'homepage/adicionar.html', {'form': form})