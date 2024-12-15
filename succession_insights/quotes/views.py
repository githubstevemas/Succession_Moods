import json
import random

from django.shortcuts import render


def quotes(request):
    # Charger les citations
    with open("../series_script/best_quotes.json", "r", encoding="utf-8") as file:
        best_quotes = json.load(file)

    random_quotes = random.sample(best_quotes, 25)

    # Liste d'images aléatoires
    random_images = [
        "/static/images/scoop-connor.png",
        "/static/images/scoop-kendal.png",
        "/static/images/scoop-roman.png",
        "/static/images/scoop-shiv.png",
        "/static/images/scoop-tom.png",
    ]

    for _ in range(min(5, len(random_images))):
        index = random.randint(0, len(random_quotes))
        image = random_images.pop()
        random_quotes.insert(index, {"Image": image})

    return render(request,
                  'quotes.html',
                  {'random_quotes': random_quotes})
