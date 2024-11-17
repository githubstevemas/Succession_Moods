import pandas as pd

from transformers import pipeline

sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)


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
