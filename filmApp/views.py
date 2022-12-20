from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Film, Category
from .forms import FilmForm


# Create your views here.
def index(request):
    films = Film.objects.all()
    return render(request, 'filmApp/index.html', {'films': films})


def add(request):
    if Category.objects.all().count() == 0:
        Category.objects.create(genre='Драма')
        Category.objects.create(genre='Ужасы')
    if request.method == 'POST':
        film = Film()
        film.name = request.POST.get('name')
        film.genre = request.POST.get('genre')
        film.issue_date = request.POST.get('issue_date')
        film.actors = request.POST.get('actors')
        film.show_date = request.POST.get('show_date')
        return redirect('home')
    else:
        categories = Category.objects.all()
        filmForm = FilmForm()
        return render(request, 'filmApp/add.html', {'form': filmForm, 'categories': categories})


def edit(request, id):
    try:
        film = Film.objects.get(id=id)
        if request.method == 'POST':
            film.name = request.POST.get('name')
            film.genre = request.POST.get('genre')
            film.issue_date = request.POST.get('issue_date')
            film.actors = request.POST.get('actors')
            film.show_date = request.POST.get('show_date')
            return redirect('home')
        else:
            categories = Category.objects.all()
            return render(request, 'edit.html', {'film': film, 'categories': categories})
    except film.DoesNotExist:
        return HttpResponseNotFound('Film not found')


def delete(request):
    return redirect('home')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
