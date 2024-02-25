#Creating an empty list called my_list.
my_list = [] 
#Appending values to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)    
print(my_list)
#Inserting a value at a specified position
my_list.insert(1, 15) 
print(my_list)
#Creating another list
another_list =[50, 60, 70] 
print(another_list)
#Extending my_list with the new list
my_list.extend(another_list) 
print(my_list)
#Removing the last item from my_list
my_list.pop(-1) 
print(my_list)
#Sorting my_list in ascending order.
my_list.sort() 
print(my_list)
#Find and print the index of the value 30 in my_list.
print(my_list.index(30))