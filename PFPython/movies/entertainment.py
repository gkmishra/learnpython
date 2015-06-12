import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story", "a story of a boy and a girl", "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print toy_story.storyline
avatar = media.Movie("Avatar", "Science fiction epic about colonizing Pandora", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
jurassicworld = media.Movie("Jurassic World", "Set 22 years after Jurassic Park", "http://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg", "https://www.youtube.com/watch?v=RFinNxS5KN4")
hungergames2 = media.Movie("The Hunger Games : Mockingjay 2", "With the nation of Panem in a full scale war, Katniss confronts President Snow in the final showdown", "http://upload.wikimedia.org/wikipedia/en/9/9d/Mockingjay_Part_2_Poster.jpg" ,"https://www.youtube.com/watch?v=5ta8izvmcTw")
madmax = media.Movie("Mad Max : Fury Road", "In a stark desert landscape where humanity is broken, two rebels just might be able to restore order", "http://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg", "https://www.youtube.com/watch?v=hEJnMQG9ev8")
sanandreas = media.Movie("San Andreas", "In the aftermath of a massive earthquake in California, a rescue-chopper pilot makes a dangerous journey across the state in order to rescue his daughter.", "http://upload.wikimedia.org/wikipedia/en/3/38/San_Andreas_poster.jpg", "https://www.youtube.com/watch?v=23VflsU3kZE")
movie_list = [avatar, jurassicworld, hungergames2, sanandreas, madmax, toy_story]
fresh_tomatoes.open_movies_page(movie_list)
