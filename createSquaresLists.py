# create squares with lists and loops then sort data 


start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number**2)

square_list.sort()
print(square_list)
