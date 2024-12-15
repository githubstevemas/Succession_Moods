import json
import os

CHARACTERS = ["LOGAN",
              "KENDAL",
              "SHIV",
              "ROMAN",
              "TOM"]


def write_best_quotes_json(quotes):

    file_path = "../../series_script/best_quotes.json"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, "r+", encoding="utf-8") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []

            existing_data.extend(quotes)

            file.seek(0)
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
            file.truncate()
    except FileNotFoundError:

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(quotes, file, ensure_ascii=False, indent=4)


def get_best_quotes(season, episode, character_name):

    try:
        with open(
                f"../../series_script/S{season}/E{episode}/{character_name}.json",
                'r', encoding="utf-8") as file:
            quotes = [json.loads(line) for line in file]

    except Exception as e:
        print(e)

    negative_quotes = []

    for quote in quotes:
        if (quote["Sentiment"] == "negative"
                and quote["Score"] > 0.90
                and quote["Dialogue"].endswith(('.', '?'))
                and quote["Dialogue"][0].isupper()):
            negative_quotes.append({
                "Dialogue": quote["Dialogue"],
                "Character": character_name,
                "Season": f"S{season}",
                "Episode": f"E{episode}"
            })

    write_best_quotes_json(negative_quotes)


def get_characters_dialogues():

    try:
        for season in range(1, 5):
            try:
                for episode in range(1, 11):
                    try:
                        for character in CHARACTERS:
                            get_best_quotes(season, episode, character)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


get_characters_dialogues()
