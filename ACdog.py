class Dog:
    # class variable (shared by all dogs)
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # instance variables (unique to each dog)
        self.name = name
        self.breed = breed

    def display_details(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)
        print("-------------------")


# creating two different dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# displaying their details
dog1.display_details()
dog2.display_details()