from succession_insights.utils.create_directories import create_dialogues_dirs
from succession_insights.utils.text_extractor import extract_text_from_pdf, \
    extract_episodes_from_season


create_dialogues_dirs()

for season in range(1, 5):

    text = extract_text_from_pdf(season)
    extract_episodes_from_season(text, season)
