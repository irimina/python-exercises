import random

# define some lists


section12A=[80,75,88,80,70,98]
section12B=[85,80,93,85,75,100]
section12C=[75,70,83,75,65,93]
section12D=[70,65,78,70,60,88]

def findMinVal(myList):
     print("Original values: ", myList)
     minVal=100
     for i in range(0,len(myList)):
          if myList[i]<minVal:
               minVal=myList[i]
     print("The smallest value in the list is ",minVal)

'''
 What value should minVal start off as?
 Set its value before your loop.
  var minVal = 100
  Set to the max possible value
  (our list is only populated with values between 0-100).
  This way, as we find values that are smaller than 100,
  our initial value of minValue will be reset to the
  ACTUAL minimum value.
'''


findMinVal(section12A)
findMinVal(section12B)
findMinVal(section12C)
