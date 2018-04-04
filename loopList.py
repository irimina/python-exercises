import random

lotteryNumbers= []
lotteryNumbers.append(random.randint(1,69))
lotteryNumbers.append(random.randint(1,69))
lotteryNumbers.append(random.randint(1,69))
lotteryNumbers.append(random.randint(1,69))
lotteryNumbers.append(random.randint(1,69))
lotteryNumbers.append(random.randint(1,69))

'''
print(lotteryNumbers)
'''
'''
# How do you print all the indexes
for i in range(0,len(lotteryNumbers)):
          print(lotteryNumbers[i]) # print all the indexes
'''
# Modify the list add the value 5 to every value in the array 
'''
print("Before: ", lotteryNumbers)

# update all the elements in the list using the for loop

for i in range(0,len(lotteryNumbers)):
     lotteryNumbers[i]= lotteryNumbers[i]+5

print("After: ",lotteryNumbers)
'''

'''
Exercises:
create a loop and:
     print all the values in the list divided by 2
     print all the squares of the numbers in the list

'''
'''
#How do you display any value in the array greater than 5 
for i in range(0,len(lotteryNumbers)):
     if lotteryNumbers[i] >25:
          print(lotteryNumbers[i])
'''










