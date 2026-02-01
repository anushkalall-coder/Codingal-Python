try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age entered is valid.")

    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")

except ValueError as e:
    print("Invalid input:", e)

except Exception:
    print("Something went wrong. Please try again.")