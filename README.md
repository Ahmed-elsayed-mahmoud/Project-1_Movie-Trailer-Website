# Movie Trailer Website

A website that allows the users to see my favorite movies and watch the trailers.

# How To Run

  - Download the code
  - Extract compressed file
  - Open terminal and cd to the extracted folder
  - Run the application by typing `python main.py`
  - This will open up a page in your web browser
  - Hover over the Movie to view short Movie Storyline
  - Click on the Movie to see youtube trailer

# Project Files

There are three main python files:

  - **main.py** - This is the main file which will call the function that generates the website and pass the movies list as a parameter.
  - **fresh_tomatoes.py** - The provided web page generator. It takes in a list of movies and builds the `HTML` and opens up
  your default browser to display the generated `HTML` page.
  - **media_movie.py** - This class provides a way to store movie related information such as the movie's title, storyline, poster image url and youtube trailer
    so it can be accessed by fresh_tomatoes.py to construct a website of movie trailers.
  

# Modules Used

    - webbrowser module
    - fresh_tomatoes.py file from Udacity's course