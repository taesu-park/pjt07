from django.shortcuts import render, get_object_or_404
from .models import Movie
from .forms import ReviewForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

def profile(request, movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    context = {
        'movie':movie
    }
    return render(request, 'movies/profile.html', context)

def review(request, movie_pk):
    
    if request.method=='POST':
        form = 
        # return redirect
    else:
