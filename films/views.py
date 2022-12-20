from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Film, Category
from .forms import FilmForm


def index(request):
    films = Film.objects.all()
    if Category.objects.count() == 0:
        Category.objects.create(name='Биография')
        Category.objects.create(name='Боевик')
        Category.objects.create(name='Детектив')
        Category.objects.create(name='Фантастика')
        Category.objects.create(name='Комедия')
    return render(request, 'index.html', {'films': films})


def add(request):
    form = FilmForm()
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add.html', {'form': form})


def edit(request, pk):
    film = get_object_or_404(Film, pk=pk)
    form = FilmForm(instance=film)
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit.html', {'form': form})


def delete(request, pk):
    film = get_object_or_404(Film, pk=pk)
    film.delete()
    return redirect('index')

