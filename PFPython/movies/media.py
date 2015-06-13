import webbrowser
class Movie():
    '''Class to provide a blueprint to store movie related details'''
    # Constructor to initialize basic information
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # function to Show the trailer of the selected movie in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
