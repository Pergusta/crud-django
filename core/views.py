from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm


def filme_list(request):
    filmes = Filme.objects.all()
    return render(request, 'core/filme_list.html', {'filmes': filmes})


def filme_detail(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    return render(request, 'core/filme_detail.html', {'filme': filme})


def filme_create(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filme_list')
    else:
        form = FilmeForm()
    return render(request, 'core/filme_form.html', {'form': form, 'titulo_pagina': 'Novo filme'})


def filme_update(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('filme_list')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'core/filme_form.html', {'form': form, 'titulo_pagina': 'Editar filme'})


def filme_delete(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        filme.delete()
        return redirect('filme_list')
    return render(request, 'core/filme_confirm_delete.html', {'filme': filme})
