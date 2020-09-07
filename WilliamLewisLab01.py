# ETGG 1801
# William Lewis
# Lab 01: name
# Date: 9/6/2020
from math import sqrt

firstName = "Will"
lastName = "Lewis"
opposite = 3.0
adjacent = 4.0

print("Lab01 created by:", firstName, lastName)
print(firstName, end=' ')
print(lastName)
hypotenuse = sqrt((opposite ** 2) + (adjacent ** 2))
print("The hypotenuse length is", hypotenuse, "if the other sides are", opposite, "and", adjacent)
input("Press Enter to continue...")

print("\n")
print("Now you get to input your own numbers!")
while True:
    oppositeEdit = int(input("Enter the opposite:"))
    adjacentEdit = int(input("Enter the adjacent:"))
    hypotenuseEdit = sqrt((oppositeEdit ** 2) + (adjacentEdit ** 2))
    print("The hypotenuse of the 2 numbers that you entered in (", oppositeEdit, end=' ')
    print("and", adjacentEdit, ") is", hypotenuseEdit)
    if hypotenuseEdit == 0:
        print("\n")
        print("\n")
        print("You've made the hypotenuse equal 0.")
        print("This marks the end of the program then.")
        print("Also, even though it's not useful outside of this context, I wish that python had labels and GOTO.")
        print("Personally, it's way more intuitive than 'while True' for something like this.")
        print("Anyway, I don't want to ramble and I spent a half hour looking for a substitute for", end=' ')
        print("creating a loop, so I need to make the github repository and turn this in.")
        print("I can't wait to see next weeks assignment and all the ways python can make me go", end=' ')
        print("'Why isn't this just built into the language?'")
        print("\n")
        print("Program created by", firstName, lastName, "for the ETGG 1801 course as Lab 01.")
        input("Press Enter to end.")
        break
    if hypotenuseEdit == 420.0214280248092:
        print("haha look guys it's the funny number")
        input("Press Enter to go again")
        print("\n")
        print("Enter your numbers!")
    else:
        input("Press Enter to go again")
        print("\n")
        print("Enter your numbers!")
