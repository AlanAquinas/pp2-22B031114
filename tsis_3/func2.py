# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#----------------------------------------------- 1
def is_above_5_5(movie):
    if movie["imdb"] > 5.5:
        return True
    else:
        return False
#----------------------------------------------- 2
def movies_are_above_5_5(movies):
    high_level_movies = []
    for i in range(len(movies)):
        movie = movies[i]
        if movie["imdb"] > 5.5:
            high_level_movies.append(movie)
    return high_level_movies
#----------------------------------------------- 3
def categorate_movies(movies, category):
    movies_by_category = []
    for i in range(len(movies)):
        movie = movies[i]
        if movie["category"] == category:
            movies_by_category.append(movie)
    return movies_by_category

#----------------------------------------------- 4

def mean_of_imdb(movies):
    sum_imdb = 0
    for movie in movies:
        sum_imdb += movie["imdb"]
    return sum_imdb / len(movies)

#----------------------------------------------- 5

def mean_of_imdb_by_category(movies, category):
    movies_by_category = categorate_movies(movies, category)
    sum_imdb = 0
    for movie in movies_by_category:
        sum_imdb += movie["imdb"]
    return sum_imdb / len(movies)