from succession_insights.utils.create_directories import create_dialogues_dirs
from succession_insights.utils.text_extractor import extract_text_from_pdf, \
    extract_episodes_from_season
from utils.analysis import episode_analysis

create_dialogues_dirs()

text = extract_text_from_pdf()
extract_episodes_from_season(text)

episode_analysis()
