# Importing Random Library
from random import *
print("Welcome To My Game")
print("Guess A Number From 0 To 10")
# A Random Number Variable
random_value=randint(0,9)
chance=0
while chance<=2:
    if chance<3:
        # Taking Number From User
        guess = int(input("Enter A Number "))
        # Comparing Both Values
        if guess == random_value:
            print("You Are Absolutely Correct")
            print("You Got It!!")
            break
        elif guess > random_value:
            print("Your Guess Was Wrong")
            print("Guess A Number Smaller Than ", guess)
            chance+=1
        elif guess < random_value:
            print("Your Guess Was Wrong")
            print("Guess A Number Greater Than ", guess)
            chance+=1
    if not chance<3:
        print("You Lost")
        print("Better Luck Next Time")
        break
# Loop Will Continue For Three Chances