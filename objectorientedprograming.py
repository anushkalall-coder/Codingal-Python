class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo= Parrot("Woo", 15)

# print("Blu is a {}".format(blu.species))
# print("Woo is a {}".format(woo.species))

# print("{} is a {} years old".format(blu.name, blu.age))
# print("{} is a {} years old".format(woo.name, woo.age))

#define a class sports with a class variable call it type(indoor or outdoor).
#define a constructor with name, number of players, country of origin
#define another method display to display the details of the sport

class Sports:
    type = "outdoor"

    def __init__(self, name, number_of_players, country_of_origin):
        self.name = name
        self.number_of_players = number_of_players
        self.country_of_origin = country_of_origin

    def display(self):
        print(f"{self.name} has {self.number_of_players} players and is originated from {self.country_of_origin}")

# soccer = Sports("Soccer", "11", "China")
# lacrosse = Sports("Lacrosse", "12", "United States of America")

# soccer.display()
# lacrosse.display()

#define a classboard game add 2 instance variables (number of players, and basic rules)
#using a display function, display the details
#create 2 objects

class BoardGame:
    
    def __init__(self, name, number_of_players, basic_rules):
        self.name=name
        self.number_of_players = number_of_players
        self.basic_rules = basic_rules
    def display(self):
        print(f"{self.name} needs {self.number_of_players} to play and the rules are {self.basic_rules}")

Monopoly = BoardGame("Monopoly", "4-6", "Move the piece across the board and earn the most money\nYou can buy or sell properties")
Chess = BoardGame("Chess", "2", "Move your pieces acorss the board and try to capture the opponents pieces\nWin the game by putting the King in checkmate")

Monopoly.display()
Chess.display()