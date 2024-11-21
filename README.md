# Movie Recommender System

A Python-based movie recommendation system that fetches movie data from The Movie Database (TMDb) API and provides random movie recommendations based on user-specified genres.

## Features

- Fetches movie data from TMDb API
- Filters movies by genre
- Stores movie data in CSV format
- Displays movie details including title, year, rating, and overview

## Prerequisites

Before running this program, you'll need to have the following installed:
- Python 3.x
- pip (Python package installer)

## Required Libraries

Install the required libraries using pip:

```bash
pip install requests
pip install pandas
pip install beautifulsoup4

Configuration

The program uses TMDb API for fetching movie data. You'll need to:

    Sign up for a TMDb account
    Get an API key
    Replace the API key in the code with your own key:

    self.api_key = "your_api_key_here"

Usage

    Run the program:

    python movie_recommendation.py

    Enter a movie genre when prompted

    The program will fetch Movie title, Release Year, Rating & Overview of that genre and provide a random recommendation

    Enter 'quit' to exit the program

Class Structure
MovieRecommender

    __init__(): Initializes the MovieRecommender with API key and data file path
    scrape_movies(genre): Fetches movies data from TMDb API for a specific genre
    read_movies_data(): Reads stored movie data from CSV file
    recommend_movie(movies): Provides a random movie recommendation

Data Storage

Movie data is stored in a CSV file named "movies_data.csv" with the following columns:

    title
    rating
    year
    overview
    genre

Error Handling

The program includes comprehensive error handling for:

    API request failures
    File operations
    Invalid user inputs
    Unexpected errors
