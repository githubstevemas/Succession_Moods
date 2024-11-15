from django.shortcuts import render


def moods(request):

    return render(request, 'moods.html')
