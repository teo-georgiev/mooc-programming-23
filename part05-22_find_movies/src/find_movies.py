# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int): 
    movie = {
        "name" : name, 
        "director" : director,
        "year" : year, 
        "runtime" : runtime
    }
    
    database.append(movie)

def find_movies(database: list, search_term: str):
    myMovies = []
    # for movie in database: 
    #     print(movie["name"])
    # print("* * *")

    tempSearch = search_term.upper()
    for movie in database: 
        tempMovie = movie["name"].upper()
        if tempMovie.find(tempSearch) >= 0: 
            myMovies.append(movie)
    return myMovies

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    
    my_movies = find_movies(database, "python")
    print(my_movies)



