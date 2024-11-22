import os

import pandas as pd
import plotly.express as px

from django.shortcuts import render


def moods(request):
    return render(request, 'moods.html')


def character_moods(request,  character_name, season="1"):
    season_sentiments = []

    for episode in range(1, 11):

        try:
            file_path = f"../series_script/S{season}/E{episode}/{character_name}.json"
            print(f"Checking: {os.path.abspath(file_path)}")
            df = pd.read_json(file_path, lines=True)

            if not df.empty:
                sentiment_counts = df['Sentiment'].value_counts(
                    normalize=True) * 100
            else:
                sentiment_counts = pd.Series(
                    {"positive": 0, "neutral": 0, "negative": 0})

            season_sentiments.append(sentiment_counts)

        except Exception as e:
            print(f"Error: {e}.")

    season_df = pd.DataFrame(season_sentiments).fillna(0)
    season_df['Episode'] = range(1, len(season_df) + 1)

    fig = px.bar(
        season_df.melt(id_vars='Episode',
                       var_name='Sentiment',
                       value_name='Percentage'),
        x='Episode',
        y='Percentage',
        color='Sentiment',
        color_discrete_map={
            "positive": "#77DD77",
            "neutral": "#FFB347",
            "negative": "#FF6961"
        },
        labels={'Episode': 'Episode ', 'Percentage': 'Percentage (%) '},
        barmode='stack'
    )

    fig.update_traces(
        hoverlabel=dict(
            bgcolor="#F7F7F7",
            font_size=12,
            font_color="black"
        )
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

    return render(request,
                  'moods.html',
                  {'graph_html': graph_html,
                   'character_name': character_name.capitalize(),
                   'season': season})
