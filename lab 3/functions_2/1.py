from movies import movies

def is_highly_rated(movie_name):
    for movie in movies:
        if movie["name"].lower() == movie_name.lower():
            return movie["imdb"] > 5.5
    return False

print(is_highly_rated(input()))
