# nested loop example to print a square and then a rectangle


for i in range(0,5):
     for i in range(0,10): # print 10 stars for 5 times 
          print("*", end="") # print the lines of stars across
     print() # go to a new line
     
'''
The order of execution for the nested loop is:

outer loop initialize variable

outer loop test condition

inner loop initialize variable

inner loop test condition

body of inner loop

inner loop update variable

repeat inner loop

outer loop update variable

repeat outer loop


'''
