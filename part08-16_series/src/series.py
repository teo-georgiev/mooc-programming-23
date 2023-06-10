# Write your solution here:
class Series: 
    def __init__(self, title: str, number_seasons: int, genres: list):
        self.title = title
        self.number_seasons = number_seasons
        self.genres = genres

        self.ratings = 0
        self.num_ratings = 0
        self.avg_rating = 0
    
    def __str__(self) -> str:
        genre_string = ", ".join(self.genres)
        if self.ratings <= 0: 
            return f"{self.title} ({self.number_seasons} seasons) \ngenres: {genre_string} \nno ratings"
        else:             
            return f'{self.title} ({self.number_seasons} seasons)\n' \
            f'genres: {genre_string}\n' \
            f'{self.num_ratings} ratings, average {self.avg_rating:.1f} points'
    
    def rate(self, rating: int): 
        self.ratings += rating
        self.num_ratings += 1 
        self.avg_rating = self.ratings / self.num_ratings

def minimum_grade(rating: float, series_list: list):
    min_grade_list = []
    for item in series_list: 
        if item.avg_rating >= rating: 
            min_grade_list.append(item)
    return min_grade_list
        
def includes_genre(genre: str, series_list: list): 
    genre_list = []
    for item in series_list: 
        if genre in item.genres:
            genre_list.append(item)
    return genre_list
        
if __name__ == "__main__": 
    series1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    series1.rate(5)

    series2 = Series("South Park", 24, ["Animation", "Comedy"])
    series2.rate(3)

    series3 = Series("Friends", 10, ["Romance", "Comedy"])
    series3.rate(2)

    series_list = [series1, series2, series3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)
    
    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)