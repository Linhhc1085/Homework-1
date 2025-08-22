# CSCI1010: Lab 1, Problem 1
# Filename: hw1pr2.py
# Name: 
# Problem description: Solving the quadratic equation!

from math import *

x = input("Supply a number: ")
x = float(x)
print("The value stored by the variable x is",x)


#Quadratic Equation
a = int(input("Supply a number for a:"))
b = int(input("Supply a number for b:"))
c = int(input ("Supply a number for c:"))

sqreroot = (b**2)-(4*a*c)
sol1 = (-b-sqrt(sqreroot))/(2*a)
sol2 = (-b+sqrt(sqreroot))/(2*a)
print ("The solution for x are", sol1, "and", sol2)