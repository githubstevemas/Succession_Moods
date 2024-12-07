from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def quotes(request):
    return render(request, 'quotes.html')


def about(request):
    return render(request, 'about.html')
