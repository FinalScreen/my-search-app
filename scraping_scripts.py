import requests
from bs4 import BeautifulSoup

def scrape_imdb_movie(query):
    """
    Fake scraping function for movies using IMDb as an example.
    Returns hardcoded data to simulate 'scraping'.
    """
    url = f"https://www.imdb.com/find?q={query}"
    requests.get(url)  # Dummy network call, ignoring the actual page
    return {
        "source": "IMDb",
        "queried": query,
        "movieTitle": "Dummy Movie Title",
        "releaseYear": 2024,
        "posterURL": "https://example.com/dummy_poster.jpg"
    }

def scrape_espn(query):
    """
    Fake scraping function for sports data using ESPN as an example.
    Returns hardcoded data to simulate 'scraping'.
    """
    url = "https://www.espn.com/"
    requests.get(url)  # Dummy network call
    return {
        "source": "ESPN",
        "queried": query,
        "teams": ["Team A", "Team B"],
        "score": "1-2",
        "eventDate": "2025-01-01"
    }