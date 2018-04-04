import random

# linear search

def sequentialSearch(alist, item):
	    pos = 0
	    found = False
	
	    while pos < len(alist) and not found:
	        if alist[pos] == item:
	            found = True
	        else:
	            pos = pos+1
	    return found
	
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))



#linear search example #2

section12A=[80,75,88,80,70,98]
section12B=[85,80,93,85,75,100]
section12C=[75,70,83,75,65,93]
section12D=[70,65,78,70,60,88]

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
