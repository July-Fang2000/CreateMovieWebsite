import fresh_tomatoes
import media

story1 = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

#print(toy_story1.storyline)
#toy_story1.show_trailer()

story2 = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

story3 = media.Movie("School of Rock",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")

story4 = media.Movie ("Ratatouille",
"Storyline",
"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
"https://www.youtube.com/watch?v=NgsQ8mVkN8w")

story5 = media.Movie( "Midnight in Paris",
"Storyline",
"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
"https://www.youtube.com/watch?v=FAfR8omt-CY")

story6 = media.Movie("Hunger Games",
"Storyline",
"https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
"https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [story1,story2,story3,story4,story5,story6]
fresh_tomatoes.open_movies_page(movies)