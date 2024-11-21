import fitz
import re

from utils.analysis import dialogue_analysis

SCRIPT_PATH = "series_script"
SCRIPT_NAME = "s01.pdf"
CHARACTERS = ["LOGAN",
              "KENDAL",
              "SHIV",
              "ROMAN",
              "TOM"]


def extract_character_text_from_episode(character,
                                        text_episode,
                                        season_nb,
                                        episode_nb):
    # Split character text from episode

    character_text = text_episode.split(character)

    character_text.pop(0)

    episode_dialogues = []

    for text in character_text:

        # Keep character dialogue from character text
        unique_text = re.split(r'[A-Z]{3,}', text)
        dialogues = unique_text[0].split("\\n")

        for dialogue in dialogues:

            if (len(dialogue) > 0
                # Clean dialogue and remove narration text

                    and dialogue.startswith("\\t")
                    and not dialogue.startswith("\\t(")):

                dialogue = dialogue.replace("\\t", "")

                if len(dialogue) > 0:

                    episode_dialogues.append(dialogue)

    df_result = dialogue_analysis(episode_dialogues)

    df_result.to_json(f"{SCRIPT_PATH}/"
                      f"S{season_nb}/"
                      f"E{episode_nb}/"
                      f"{character}.json",
                      orient="records",
                      lines=True)


def extract_episodes_from_season(season_text, season_nb):
    # Extract episode text from an entire season

    episodes_text = season_text.split("Episode ")
    episodes_text.pop(0)

    episode_nb = 0

    for episode in episodes_text:

        episode_nb += 1

        for character_nb in range(len(CHARACTERS)):

            extract_character_text_from_episode(CHARACTERS[character_nb],
                                                episode,
                                                season_nb,
                                                episode_nb)

    return


def extract_text_from_pdf(season_nb):
    # Extract text from pdf script with pdfplumber

    text = ""

    try:
        with fitz.open(f"{SCRIPT_PATH}/s0{season_nb}.pdf") as pdf:
            for page_num in range(pdf.page_count):
                page = pdf[page_num]
                blocks = page.get_text("blocks")

                for block in blocks:
                    x0, y0, x1, y1, contenu, *_ = block
                    lignes = contenu.splitlines()

                    if x0 > 100:
                        for ligne in lignes:
                            text += f"\\t{ligne}\\n"
                    else:
                        for ligne in lignes:
                            text += f"{ligne}\\n"

                text += "\\n"

    except Exception as e:
        print("Scripts not found in 'series_script' directory")
        print(e)

    return text
