# review functions basic
'''
task:define a function with one argument
  If the type of the argument is either int or float, the function should return the absolute value of the function input.
  Otherwise, the function should return "Nope"
'''
'''
from math import*

def distance_from_zero(a):
  if type(a)==int or type(a)==float:
    return abs(a)
  else:
    return("Nope")
'''
