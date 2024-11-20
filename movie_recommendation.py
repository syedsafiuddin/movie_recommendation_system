import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
import time
import os

class MovieRecommender:
    def __init__(self):
        self.api_key = "d3cfc4eed8a0280ba2ca73ce7094af3a"
        self.data_file = "movies_data.csv"
        
    def scrape_movies(self, genre):
        """Scrape movies data from TMDb and save to CSV"""
        try:
            # Get genre ID
            genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.api_key}&language=en-US"
            genre_response = requests.get(genre_url)
            genre_response.raise_for_status()  # Check for HTTP errors
            genres = genre_response.json().get('genres', [])

            genre_id = None
            for g in genres:
                if g['name'].lower() == genre.lower():
                    genre_id = g['id']
                    break

            if genre_id is None:
                raise ValueError(f"Genre '{genre}' not found")

            # Get movies for the genre
            movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&with_genres={genre_id}"
            movies_response = requests.get(movies_url)
            movies_response.raise_for_status()
            results = movies_response.json().get('results', [])

            # Create list of movies
            movies_data = []
            for movie in results:
                movies_data.append({
                    'title': movie.get('title', ''),
                    'rating': movie.get('vote_average', 0),
                    'year': movie.get('release_date', '')[:4],
                    'overview': movie.get('overview', ''),
                    'genre': genre
                })

            # Save to CSV
            df = pd.DataFrame(movies_data)
            df.to_csv(self.data_file, index=False)
            return True

        except requests.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def read_movies_data(self):
        """Read movies data from CSV using Pandas"""
        try:
            if not os.path.exists(self.data_file):
                raise FileNotFoundError("Movies data file not found")
            
            df = pd.read_csv(self.data_file)
            return df.to_dict('records')

        except FileNotFoundError as e:
            print(f"Error: {e}")
            return []
        except Exception as e:
            print(f"Error reading data: {e}")
            return []

    def recommend_movie(self, movies):
        """Recommend a random movie from the list"""
        try:
            if not movies:
                raise ValueError("No movies available for recommendation")
            
            movie = random.choice(movies)
            return (f"\nRecommended Movie: {movie['title']} ({movie['year']})"
                   f"\nRating: {movie['rating']}/10"
                   f"\nOverview: {movie['overview']}")

        except Exception as e:
            return f"Error making recommendation: {e}"


def main():
    try:
        recommender = MovieRecommender()
        
        print("\nWelcome to Movie Recommender!")
        while True:
            genre = input("\nEnter a genre (or 'quit' to exit): ").strip().lower()
            
            if genre == 'quit':
                print("Thank you for using Movie Recommender!")
                break
                
            if not genre:
                print("Please enter a valid genre")
                continue

            # Scrape and save data
            print("Fetching movies data...")
            if recommender.scrape_movies(genre):
                print("Data successfully retrieved")
                # Read data and make recommendation
                movies = recommender.read_movies_data()
                if movies:
                    recommendation = recommender.recommend_movie(movies)
                    print(recommendation)
                else:
                    print("No movies data available")
            else:
                print("Failed to retrieve data")

    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
