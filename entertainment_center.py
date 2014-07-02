import media
import fresh_tomatoes

movie_title = "Toy Story"
movie_storyline = "A story of a boy and his toys that come to life"
poster_image = "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=vwyZH85NQC4"
###
toy_story = media.Movie(movie_title, movie_storyline, poster_image, trailer_youtube)

movie_title = "Avatar"
movie_storyline = "A marine on an alien planet"
poster_image = "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=-9ceBgWV8io"
###
avatar = media.Movie(movie_title, movie_storyline, poster_image, trailer_youtube)

movie_title = "Batman Begins"
movie_storyline = """
                        When his parents were killed, millionaire playboy Bruce Wayne relocates to Asia
                        when he is mentored by Henri Ducard and Ra's Al Ghul in how to fight evil.
                        When learning about the plan to wipe out evil in Gotham City by Ducard,
                        Bruce prevents this plan from getting any further and heads back to his home.
                        Back in his original surroundings, Bruce adopts the image of a bat to strike fear into
                        the criminals and the corrupt as the icon known as 'Batman'.
                        But it doesn't stay quiet for long."""
poster_image = "http://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=vak9ZLfhGnQ"
###
batman_begins = media.Movie(movie_title, movie_storyline, poster_image, trailer_youtube)

movie_title = "The Dark Knight"
movie_storyline = """Batman raises the stakes in his war on crime. With the help of Lieutenant Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the city streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as The Joker."""
poster_image = "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=yQ5U8suTUw0"
###
dark_knight = media.Movie(movie_title, movie_storyline, poster_image, trailer_youtube)

movie_title = "The Dark Knight Rises"
movie_storyline = """Despite his tarnished reputation after the events of The Dark Knight, in which he took the rap for Dent's crimes, Batman feels compelled to intervene to assist the city and its police force which is struggling to cope with Bane's plans to destroy the city."""
poster_image = "http://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=GokKUqLcvD8"
###
dark_knight_rises = media.Movie(movie_title, movie_storyline, poster_image, trailer_youtube)

movie_title = "Midnight in Paris"
movie_storyline = """Going back in time to meet authors"""
poster_image = "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=atLg2wQQxvU"
###
midnight_in_paris = media.Movie(movie_title, movie_storyline, poster_image, trailer_youtube)

movies = [toy_story, avatar, batman_begins, dark_knight, dark_knight_rises, midnight_in_paris]

fresh_tomatoes.open_movies_page(movies)









