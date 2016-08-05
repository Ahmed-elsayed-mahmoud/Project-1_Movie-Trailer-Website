class Movie:
    """
    This class  provides a way to store movie related information such as the movie's title, storyline, poster image url and youtube trailer
    so it can be accessed by fresh_tomatoes.py to construct a website of movie trailers.
    """
    
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
