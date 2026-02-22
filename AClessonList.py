start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

even_squares = []
odd_squares = []

for num in range(start, end + 1):
    square = num ** 2
    
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("\nEven square values:")
print(even_squares)

print("\nOdd square values:")
print(odd_squares)