from hd.models import Genre
from django.shortcuts import render


def show_genres(request):
    return render(request, "index.html", {'genres': Genre.objects.all()})
