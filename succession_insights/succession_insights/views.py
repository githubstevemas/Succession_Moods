from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def seasons(request):
    return render(request, 'seasons.html')


def about(request):
    return render(request, 'about.html')
