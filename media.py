import webbrowser
class Movie():
    """Class that is a container for movies. Used with fresh_tomatoes.py to generate an html page displaying movies. """
##    def __init__():
##        self.title = ""
##        self.storyline = ""
##        self.poster_image = ""
##        self.trailer_youtube_url = ""
    MOVIE_RATING = ["G", "PG", "PG-13", "R"]    

    #isntance methods all take self as first arg
    def __init__(self, title, storyline, image_url, youtube_url):
        self.title = title
        self.story_line = storyline
        self.poster_image = image_url
        self.trailer_youtube_url = youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
