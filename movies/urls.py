from django.urls import path
from . import views
app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.profile, name='profile'),
    path('<int:movie_pk>/reviews/new', views.review, name='review'),
]
