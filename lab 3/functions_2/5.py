from movies import movies

def average_imdb_by_category(category):
    filtered_movies = [movie for movie in movies if movie["category"].lower() == category.lower()]
    return sum(movie["imdb"] for movie in filtered_movies) / len(filtered_movies) if filtered_movies else 0

print(average_imdb_by_category(input()))
