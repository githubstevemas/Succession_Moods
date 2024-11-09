# Succession Character Emotion Analysis

This project is a Django-based web application that leverages Natural Language Processing (NLP) techniques to analyze and visualize the emotional tones of characters from HBO’s Succession. By processing and interpreting dialogue data, this tool reveals insights into the underlying emotions and sentiments of each character throughout the series, providing fans and analysts with a deeper understanding of character development and relationships.

<br>

## Features

- **Character Emotion Analysis**: Uses NLP to extract emotional tone from dialogue and attributes it to individual characters.
- **Data Visualization**: Interactive visualizations of emotional trends and shifts for each character.
- **Character Comparison**: Compare emotional trends across multiple characters to see dynamics and contrast over time.
- **Episode and Season Filtering**: Analyze emotional changes episode-by-episode or across entire seasons.

<br>

## Technologies Used

- [Django](https://www.djangoproject.com/) : Web framework used to build the backend and handle routing.
- [NLTK](https://www.nltk.org/) : Natural Language Toolkit for text processing and sentiment analysis.
- [Matplotlib](https://matplotlib.org/) : Visualization library for creating sentiment trend charts and emotional graphs.
- [Plotly](https://plotly.com/) : Interactive graphing library for enhanced user interaction with visual data.

<br>

## How to Run

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

Start the development server:
```
python manage.py runserver
```

Then, open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

<br>

## Contact
For any questions, feedback, or contributions, please reach out:

Email: mas.ste@gmail.com
