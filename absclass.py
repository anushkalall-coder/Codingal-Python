# from abc import ABC, abstractmethod

# class Absclass(ABC):

#     def print(self,x):
#         print("Passed value: ", x)

#         @abstractmethod
#         def task(self):
#             print("We are inside Absclass task")

# class test_class(Absclass):
#     def task(self):
#         print("We are inside test_class task")

# test_obj = test_class()
# test_obj.task()
# test_obj.print(100)

#Code 2

# class Animal(ABC):

#     def move(self):
#         pass

# class Human(Animal):

#     def move(self):
#         print("I can crawl")

# class Dog(Animal):

#     def move(self):
#         print("I can bark")

# class Lion(Animal):

#     def move(self):
#         print("I can roar")

# R = Human()
# R.move()

# R = Dog()
# R.move()

# K =Lion()
# K.move()

# Code 3

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of the USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind=India()
obj_usa=USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()