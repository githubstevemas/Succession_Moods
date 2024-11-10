import fitz
import re

SCRIPT_PATH = "series_script"
SCRIPT_NAME = "s01.pdf"
CHARACTERS = ["LOGAN",
              "KENDAL",
              "MARCIA",
              "SHIV",
              "GREG",
              "LAWRENCE",
              "ROMAN",
              "CONNOR"]


def extract_character_text_from_episode(character, text_episode, episode_nb):

    # Split character text from episode
    character_text = text_episode.split(character)

    character_text.pop(0)

    character_dialogues = (
        open(f"{SCRIPT_PATH}/S1/E{episode_nb}/{character}.txt", "wb"))

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
                    character_dialogues.write(dialogue.encode("utf8"))


def extract_episodes_from_season(season_text):
    # Extract episode text from an entire season

    episodes_text = season_text.split("Episode ")
    episodes_text.pop(0)

    episode_nb = 0

    for episode in episodes_text:

        episode_nb += 1

        for character_nb in range(len(CHARACTERS)):

            extract_character_text_from_episode(CHARACTERS[character_nb],
                                                episode,
                                                episode_nb)

    return


def extract_text_from_pdf():
    # Extract text from pdf script with pdfplumber

    text = ""

    try:

        with fitz.open(f"{SCRIPT_PATH}/{SCRIPT_NAME}") as pdf:
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
        print(e)

    return text
