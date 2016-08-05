import media_movie
import fresh_tomatoes
"""
This is the main file which will call the function that generates the website and pass the movies list as a parameter.
"""

# Create instances of the Movie class to hold information of my favourite movies

toy_story = media_movie.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media_movie.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://smellslikescreenspirit.com/wp-content/uploads/2009/08/AvatarTeaserPoster-460x687.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

ratatouille = media_movie.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media_movie.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media_movie.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

matrix = media_movie.Movie("Matrix",
                     "A movie about the reality of life itself.",
                     "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")


seven_lucky_kids = media_movie.Movie("7 Lucky Kids",
                               "Seven kids with superior martial arts skills stumble into excitement and adventure",
                               "http://ia.media-imdb.com/images/M/MV5BMTI5MTg1NTIzOV5BMl5BanBnXkFtZTYwNDg2Njg4._V1__SX640_SY720_.jpg",
                               "https://www.youtube.com/watch?v=MYXNpYexk1A")

in_a_world = media_movie.Movie("In a World",
                         "Story Line.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/4/49/In_a_World_poster.jpg/220px-In_a_World_poster.jpg",
                         "https://www.youtube.com/watch?v=bZHBjLFu5is")

pi = media_movie.Movie("Pi",
                 "Story Line.",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Piposter.jpg/220px-Piposter.jpg",
                 "https://www.youtube.com/watch?v=jo18VIoR2xU")

# Add all the instances of movies into a list
movies = [
    toy_story,
    avatar,
    ratatouille,
    midnight_in_paris,
    hunger_games,
    matrix,
    seven_lucky_kids,
    in_a_world,
    pi
    ]

# Call the fresh_tomatoes to do its magic, build the website and display the movies
fresh_tomatoes.open_movies_page(movies)
