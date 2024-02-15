#!/usr/bin/node
import sys
import requests

def get_movie_characters(movie_id):
    film_url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(film_url)
    if response.status_code == 200:
        film_data = response.json()
        character_urls = film_data['characters']
        characters = []
        for url in character_urls:
            character_response = requests.get(url)
            if character_response.status_code == 200:
                character_data = character_response.json()
                characters.append(character_data['name'])
            else:
                print(f"Failed to fetch character data from {url}")
        return characters
    else:
        print(f"Failed to fetch film data from {film_url}")
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <movie_id>")
        sys.exit(1)
    
    movie_id = sys.argv[1]
    characters = get_movie_characters(movie_id)
    if characters:
        for character in characters:
            print(character)
    else:
        print("No characters found for the given movie ID.")
