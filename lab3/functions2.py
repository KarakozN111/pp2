movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

#ex1
def is_high_score(movie_name, movies):
    for movie in movies:
        if movie['name'] == movie_name:
            return movie['imdb'] > 5.5
    return False
movie_name = input("Write the name of the movie: ")
print(is_high_score(movie_name, movies))

#ex2
def get_high_score_movies(movies):
    high_score_movies = [movie for movie in movies if movie['imdb'] > 5.5]
    return high_score_movies

high_score_movies = get_high_score_movies(movies)
print("Movies with an IMDB score above 5.5:")
for movie in high_score_movies:
    print(movie['name'])

#ex3
def get_movies_by_category(category_name, movies):
    category_movies = [movie for movie in movies if movie['category'] == category_name]
    return category_movies

category_name = input("Write the category name: ")
category_movies = get_movies_by_category(category_name, movies)
print(f"Movies under the category '{category_name}':")
for movie in category_movies:
    print(movie['name'])

#ex4
def average_imdb_score(movies):
    if not movies:
        return 0  
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)
avg_score = average_imdb_score(movies)
print(f"Average IMDB score: {avg_score}")

#ex5
def average_imdb_score_by_category(category, movies):
    category_movies = [movie for movie in movies if movie['category'] == category]
    if not category_movies:
        return 0 
    total_score = sum(movie['imdb'] for movie in category_movies)
    return total_score / len(category_movies)
category = input("Write the category name: ")
avg_score = average_imdb_score_by_category(category, movies)
print(f"Average category IMDB score '{category}': {avg_score}")  