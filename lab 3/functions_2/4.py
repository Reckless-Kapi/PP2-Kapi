from movies import movies

def average_imdb():
    return sum(movie["imdb"] for movie in movies) / len(movies)

print(average_imdb())
