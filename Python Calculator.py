# Importing Mtah Module
from math import *
# Defining Function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Welcome To My Calculator")
print("Enter Your Choice")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
# Taking Values From Users
x = int(input("Enter Your Choice "))
a = float(input("Enter First Number "))
b = float(input("Enter Second Number "))
if x==1:
    print(a ,"+", b ,"=",add(a,b))
elif x==2:
    print(a, "-", b ,"=",sub(a,b))
elif x==3:
    print(a, "*" ,b, "=",mul(a,b))
elif x==4:
    print(a ,"/" ,b,"=",div(a,b))
print("Thanks For Visiting")
# This Is A Simple Calcutor
# To Use It Again Run It Again