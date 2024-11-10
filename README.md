# Succession Moods

This project is a Django-based web application that leverages Natural Language Processing (NLP) techniques to analyze and visualize the emotional tones of characters from HBO’s Succession. By processing and interpreting dialogue data, this tool reveals insights into the underlying emotions and sentiments of each character throughout the series, providing fans and analysts with a deeper understanding of character development and relationships.

<br>

## Features to Come

- **Character Emotion Analysis**: Uses NLP to extract emotional tone from dialogue and attributes it to individual characters.
- **Data Visualization**: Interactive visualizations of emotional trends and shifts for each character.
- **Character Comparison**: Compare emotional trends across multiple characters to see dynamics and contrast over time.
- **Episode and Season Filtering**: Analyze emotional changes episode-by-episode or across entire seasons.

<br>

## Technologies Used

- [Django](https://www.djangoproject.com/) : Web framework used to build the backend and handle routing.
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) : Python library for data extraction from PDF file.

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

# How to Run

- Get series script (can be buyed from [Amazon.com](https://www.amazon.com)).
- Place pdf script in ``series_script`` root folder (file must be renamed ``s01.pdf``).
- Run ``python main.py`` for dialogue extraction from script.
- Start development server with ``python manage.py runserver``.
- Then, open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

<br>

## Contact
For any questions, feedback, or contributions, please reach out:

Email: mas.ste@gmail.com
