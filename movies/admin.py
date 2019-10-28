from django.contrib import admin
from .models import Genre, Movie
# Register your models here.
class Genreadmin(admin.ModelAdmin):
    list_display = ('id', 'name')
class Movieadmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'audience')

admin.site.register(Genre, Genreadmin)
admin.site.register(Movie, Movieadmin)