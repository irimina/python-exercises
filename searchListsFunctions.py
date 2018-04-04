import random

# define some lists


section12A=[80,75,88,80,70,98]
section12B=[85,80,93,85,75,100]
section12C=[75,70,83,75,65,93]
section12D=[70,65,78,70,60,88]

'''
def search(myList):
     flag = False

     # use list parameter not the actual list name
     for i in range(0,len(myList)):
          if myList[i]==100:
               flag=True
     print("The list contains a 90",flag)
     
     
search(section12A)
search(section12B)
search(section12C)
'''
####################################
#step 2
'''
General Search
In order to make a general search function, we should be able to search
for any value, not just 90.
We can do this by making the value to search for a parameter as well.
'''
def search(myList,searchValue):
     found = False

     # use list parameter not the actual list name
     for i in range(len(myList)):
          if myList[i]==searchValue:
               found=True
     print("The list contains a 90",found)
         
search(section12A,98)
search(section12B,77)
search(section12C,88)

'''
Reusing a Function Pattern: Find Minimum
Nice work! You've just written a function that implements an algorithm
to process an array! If you feel comfortable with the basic pattern you used
to create this function, you can quickly
create functions for many other useful algorithms that work on lists.
'''





