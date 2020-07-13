#importing Random Library
from random import *
print("Welcome To My Game")
# Random Value From Computer
print("Enter 'Yes' To Play Again And 'No' To Quit")
enter = input("Enter ")
num=randint(1,6)
if enter=="Yes":
    if num == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if num == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if num == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if num == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if num == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if num == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
else:
    print("Thankx For Visiting!!")
# Dice Will Only Role For Once
# If You Want To Play Again Run It Again
