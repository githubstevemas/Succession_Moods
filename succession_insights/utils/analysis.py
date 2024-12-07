import json
import os

import pandas as pd

from transformers import pipeline

CHARACTERS = ["LOGAN",
              "KENDAL",
              "SHIV",
              "ROMAN",
              "TOM"]

sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)


def episode_analysis(season, character):
    # From season and character return sentiments counts list

    episode_sentiment_counts = []

    for episode in range(1, 11):

        try:
            file_path = f'series_script/S{season}/E{episode}/{character}.json'
            with open(file_path, 'r') as f:
                data = [json.loads(line) for line in f]

            sentiments = [entry['Sentiment'] for entry in data]

            # Sentiment per cent count
            sentiment_counts = {
                sentiment: (sentiments.count(sentiment) / len(
                    sentiments)) * 100
                for sentiment in set(sentiments)
            }

            episode_sentiment_counts.append(sentiment_counts)

        except Exception as e:
            print(f"{e} for S{season}/E{episode}/{character}.json")

    return episode_sentiment_counts


def seasons_analysis():
    # From all episodes get sentiments average

    for season in range(1, 5):

        output_dir = f"series_script/S{season}"
        season_sentiment_averages = {}

        for character in CHARACTERS:

            episode_sentiment_counts = episode_analysis(season, character)

            all_sentiments = ["positive", "neutral", "negative"]

            try:
                averages = {
                    sentiment: sum(
                        episode.get(sentiment, 0) for episode in
                        episode_sentiment_counts
                    ) / len(episode_sentiment_counts)
                    for sentiment in all_sentiments
                }

                season_sentiment_averages[character] = averages

            except Exception as e:
                print(e)

        output_file = os.path.join(output_dir, "averages.json")

        with open(output_file, 'w') as f:
            json.dump(season_sentiment_averages, f, indent=4)


def dialogue_analysis(dialogues):
    # Use HuggingFace for episode dialogues analysis, return a dataframe

    result = []
    for dialogue in dialogues:
        sentiment = sentiment_analyzer(dialogue)[0]

        result.append({
            "Dialogue": dialogue,
            "Sentiment": sentiment['label'],
            "Score": sentiment['score']
        })

    df = pd.DataFrame(result)

    return df
