import os
from pathlib import Path


def create_dialogues_dirs():

    project_root = Path(__file__).resolve().parent.parent.parent
    script_dir = project_root / "series_script/S1"

    if not os.path.exists(script_dir):
        os.makedirs(script_dir)

        for episode in range(10):
            os.makedirs(f"{script_dir}/E{episode + 1}")


create_dialogues_dirs()