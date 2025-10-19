print("Welcome to Anushka's Restraunt!")
print("Here is our menu")
print("1. 🍣Salmon $80")
print("2. 🍝Pasta $25")
print("3. 🍗Chicken Skewers $20")

order = int(input("Which number out of the three would you like to order?: "))

if order == 1:
    print("You chose the Salmon🍣")
    price = 80
elif order == 2:
    print("You chose Pasta🍝")
    price = 25
elif order == 3:
    print("You chose the Chicken Skewers🍗")
    price = 20
else:
    print("Invalid Entry, Try Again")
    price=0

if price > 0:
    number= int(input("How much of that order would you like?"))
    total=price*number
    print("Your total bill is ",total, ". Thank you for coming!")