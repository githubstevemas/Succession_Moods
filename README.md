<p align="center">
  <img src="https://github.com/githubstevemas/Succession_Moods/actions/workflows/ci.yml/badge.svg" alt="Build Status">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Docker%20Image-Available-green">
  <img src="https://img.shields.io/badge/Render-Live-green" alt="https://succession-moods.onrender.com">

</p>

# Succession Moods

<div align="center">
  <img src="https://github.com/githubstevemas/Succession_Moods/blob/main/succession_insights/static/images/hero.png" alt="Succession moods hero banner" width="400">
</div>

<br>

This project is a Django-based web application that leverages Natural Language Processing (NLP) techniques to analyze and visualize the emotional tones of characters from HBO’s Succession. By processing and interpreting dialogue data, this tool reveals insights into the underlying emotions and sentiments of each character throughout the series, providing fans and analysts with a deeper understanding of character development and relationships.

Try here : [https://succession-moods.onrender.com](https://succession-moods.onrender.com)

<br>

## Features

- **Character Emotion Analysis**: Uses NLP to extract emotional tone from dialogue and attributes it to individual characters.
- **Data Visualization**: Interactive visualizations of emotional trends and shifts for each character.
- **Character Comparison**: Compare emotional trends across multiple characters to see dynamics and contrast over time.

<br>

## Technologies Used

- [Django](https://www.djangoproject.com/) : Web framework used to build the backend and handle routing.
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) : Python library for data extraction from PDF file.
- [HuggingFace](https://huggingface.co/) : Powerful NLP library providing pre-trained models for sentiment analysis and text generation.
- [Pandas](https://pandas.pydata.org/) : Versatile data analysis library for data manipulation, cleaning, and transformation in Python.
- [Plotly](https://github.com/plotly/plotly.py) : Python library for creating interactive and dynamic data visualizations
- [Docker](https://www.docker.com/) : Share, and run container applications.

<br>

## How to Set

Clone the repository:
```
git clone https://github.com/githubstevemas/Succession_Moods.git
```

Navigate to the project directory:
```
cd Succession_Moods
```

Set up a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required dependencies:

```
pip install -r requirements.txt
```

Run migrations:
```
python manage.py migrate
```

<br>

## How to Run

- Get series script (can be buyed from [Amazon.com](https://www.amazon.com)).
- Place pdf scripts in ``series_script`` root folder (files must be renamed ``s01.pdf``, ``s02.pdf``, ``s03.pdf``, ``s04.pdf``).
- Run ``python main.py`` for dialogue extraction from script.
- Start development server with ``python manage.py runserver``.
- Then, open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

<br>

## Screenshots

<br>

<div align="center">
  <img src="https://github.com/githubstevemas/Succession_Moods/blob/main/succession_insights/static/images/screens/screenshot_01.png" alt="Succession moods screeshot 01" width="400">
</div>

<br>

<div align="center">
  <img src="https://github.com/githubstevemas/Succession_Moods/blob/main/succession_insights/static/images/screens/screenshot_02.png" alt="Succession moods screeshot 01" width="400">
</div>

<div align="center">
  <img src="https://github.com/githubstevemas/Succession_Moods/blob/main/succession_insights/static/images/screens/screenshot_03.png" alt="Succession moods screeshot 01" width="400">
</div>

<div align="center">
  <img src="https://github.com/githubstevemas/Succession_Moods/blob/main/succession_insights/static/images/screens/screenshot_04.png" alt="Succession moods screeshot 01" width="400">
</div>

<br>

## Upcoming Features

- 

<br>

## Disclaimer

This project is a fan project and is not affiliated with Succession, HBO, or its creators. All rights to Succession, including characters, images, and other related elements, belong to HBO and their respective creators. This project is intended for personal and educational purposes only, with no intent to infringe on these rights.

<br>

## Contact

For any questions, feedback, or contributions, please reach out:

Email: mas.ste@gmail.com
