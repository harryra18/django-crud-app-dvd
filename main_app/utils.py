import requests
import os

def fetch_movie_image(title):
    api_key = os.environ.get("OMDB_API_KEY")
    if not api_key:
        return None

    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("Response") == "True":
        return data.get("Poster")

    return None