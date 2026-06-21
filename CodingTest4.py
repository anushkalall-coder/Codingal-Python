class Book:
    def __init__ (self,title,author):
        self.title = title
        self.author=author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed =True
        print(f"Confirmation: '{self.title}' has been borrowed")
    
    def return_book(self):
        self.is_borrowed = False
        print(f"Confirmation: '{self.title}' has been returned")

book1 = Book("1984", "George Owell")
book2 = Book("Better than the movies", "Lynn Painter")
book3 = Book("Percy Jackson and the Lightning Thief", "Rick Riordan")

book1.borrow()
book1.return_book()

book2.borrow()
book3.borrow()
