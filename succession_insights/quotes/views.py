import json
import os
import random

from django.shortcuts import render


def quotes(request):
    # Charger les citations

    if os.getenv('ENV') == 'prod':
        file_path = "/app/series_script/"
    else:
        file_path = "../series_script/"

    try:
        with (open(f"{file_path}best_quotes.json", 'r', encoding='utf-8')
              as file):
            best_quotes = json.load(file)

    except Exception as e:
        print(f"Error: {e}.")

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
