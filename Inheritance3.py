class Netflix():

    def __init__(self,language,genre):
        self.language=language
        self.genre=genre

    def display(self):
        print(f"Language: {self.language}")
        print(f"Genre: {self.genre}")

class Series(Netflix):
    def __init__(self,language,genre,episodes,totalrunTime):
        super().__init__(language, genre)
        self.episodes=episodes
        self.totalrunTime= totalrunTime
    
    def display_series(self):
        print(f"Episodes: {self.episodes}")
        print(f"Total Run Time: {self.totalrunTime}")
    
class Movies(Netflix):
    def __init__(self,language,genre,totalrunTime,rating):
        super().__init__(language, genre)
        self.rating=rating
        self.totalrunTime= totalrunTime

    def display_movies(self):
        print(f"Rating: {self.rating}")
        print(f"Total Run Time: {self.totalrunTime}")

show=Series("Spanish", "Action", "25", "9 hours" )
show1=Movies("English", "Sci-Fi", "3 hours", "8/10" )

show.display()
show.display_series()
show1.display()
show1.display_movies()