# calculator 1 using variables 

welcome = input("This app calculates miles per gallon. Hit Return/Enter to continue:")

# This code almost works because of the missing float 
miles_driven = input("Enter miles driven:")
gallons_used = input("Enter gallons used:")

miles_driven = float(miles_driven)
gallons_used = float(gallons_used)

mpg = miles_driven/gallons_used

round(mpg)
print("Miles per gallon:", mpg)

# calculator 2 by adding more functions available in the math library 

from math import *

number1 = input("Enter a number: ")
number2 = input("Enter the second number: ")

x = sin(float(number1))  + cos(float(number2))
print(round(x,2))

