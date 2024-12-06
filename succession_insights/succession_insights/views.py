import json
import os
import random

import pandas as pd
import plotly.express as px

from django.shortcuts import render


def index(request):

    return render(request, 'home.html')


def seasons(request):

    return render(request, 'seasons.html')


def character_seasons(request, character_name, season="1"):

    file_path = f"../series_script/S{season}/averages.json"

    df = pd.read_json(file_path)

    character_name = character_name.upper()

    character_data = df[character_name]

    character_data = character_data.to_dict()

    labels = list(character_data.keys())
    values = list(character_data.values())

    fig = px.pie(
        names=labels,
        values=values,
        color=labels,
        color_discrete_map={
            "positive": "#77DD77",
            "neutral": "#FFB347",
            "negative": "#FF6961"
        },
    )

    fig.update_traces(
        hoverlabel=dict(
            bgcolor="#F7F7F7",
            font_size=12,
            font_color="black"
        ),
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(
            l=20,
            r=10,
            t=30,
            b=40
        )
    )

    graph_html = fig.to_html(full_html=False, config={'displayModeBar': False})

    return render(request, 'seasons.html',
                  {'graph_html': graph_html,
                   'character_name': character_name.capitalize(),
                   'season': season})


def quotes(request):
    return render(request, 'quotes.html')


def about(request):
    return render(request, 'about.html')
