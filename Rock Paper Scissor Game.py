# Importing Random Library
from random import *
# Reference To Number
# 1 = Rock
# 2 = Paper
# 3 = Scissor
print("Welcome To My Game")
print("Enter Your Choice ")
print("1. Rock")
print("2. Paper")
print("3. Scissor")
l=randint(1,3)
user=int(input("Enter Your Choice "))
if user<=3:

        if l==user:
            print("Computer's Choice is ",l)
            print("Its Tie")
            print("Play Again")
        elif l==1 and user==2:
            print("Computer's Choice is ", l)
            print("You Won")
            print("Congoo")
        elif l==1 and user==3:
            print("Computer's Choice is ", l)
            print("You Lost")
            print("Try Again")
        elif l==2 and user==1:
            print("Computer's Choice is ", l)
            print("You Lost")
            print("Try Again")
        elif l==2 and user==3:
            print("Computer's Choice is ", l)
            print("You Won")
            print("Congoo")
        elif l==3 and user==1:
            print("Computer's Choice is ", l)
            print("You Won")
            print("Congoo")
        elif l==3 and user==2:
            print("Computer's Choice is ", l)
            print("You Lost")
            print("Try Again")
else:
    print("Out Of Choice")
print("Thanks For Visiting")