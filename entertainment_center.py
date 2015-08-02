#using class from here
import media 
import fresh_tomatoes

##test = media.Movie() #module.ClassName()

toy_story = media.Movie("Toy Story",
                        "Story about toys.",
                        "https://upload.wikimedia.org/wikipedia/commons/4/46/Toy_Story.svg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


                        
#print(toy_story.story_line)

avatar = media.Movie("Avatar",
                     "human saves other plant, nice visuals",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#print(avatar.trailer_youtube_url)

#avatar.show_trailer()

big_lebowski = media.Movie("The Big Lebowski",
                           "The Dude goes on an adventure.",
                           "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/The_Big_Lebowski.svg/2000px-The_Big_Lebowski.svg.png",
                           "https://www.youtube.com/watch?v=knxhiwUspsA")

#big_lebowski.show_trailer()
#print(big_lebowski.title())                           


movies = [big_lebowski, avatar, toy_story]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.MOVIE_RATING)
