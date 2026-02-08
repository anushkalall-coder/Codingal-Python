#Activity 1

def match_words(words):
    ctr = 0
    list = []
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr += 1
            list.append(word)
    print("List of words that have the same first and last character:\n ", list)
    return ctr

count = match_words(["nan", "dad", "lmo", "mother", "585"])
print("Number of words that have the same first and last character: ",count)

#Activity 2

list=[1,2,3,4,5,7,8,9,167]
print("OG list: ", list)

count = 0

for i in list:
    count += i

avg = count/len(list)

print("sum= ", count)
print("average = ", avg)

list.sort()

print("Smallest element is ", list[0])
print("Largest element is ", list[-1])

#Activity 3

library=["Fourth Wing", "BTTM", "Percy Jackson", "Binding 13", "Powerless"]
print("Welcome to the library! \n What would you like to do?")
print("1.View our collection \n 2. Return a book \n 3. Check out a book")

ch=int(input("Enter your choice here: "))
if ch==1:
    print("The books in our library are: ")
    for i in library:
        print (i)
elif ch==2:
    book=input("Enter the name of the book you would like to return: ")
    library.append(book)
    print("Thanks for the book! The book list is here: ")
    for i in library:
        print (i)
elif ch==3:
    book=input("What book would you like to check out?")
    library.remove(book)
    print("We'll miss our book! The books list is here: ")
    for i in library:
        print (i)
else:
    print("Choose an option!")