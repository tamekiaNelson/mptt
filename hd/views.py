from hd.models import File
from django.shortcuts import render


def show_files(request):
    return render(request, "index.html", {'files': File.objects.all()})
