#  lists in python

"""
A list is a built-in data structure in python used to store multiple items ina a singel variable.

variable_name = [item1, item2, item3, ...]
"""

my_list = [10, 20, 30, 40]
print(my_list)

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Accessing Items
#          [0]       [1]       [2]   etc.
fruits =["apple", "banana", "cherry",]
print(fruits[1]) #second item
print(fruits[2]) # third item

print(fruits[-1])  # use -1 to access the last item in the list 
print(fruits[-2])  # 2nd to last item in the list

# slicing lists
print(fruits[0:2]) #items 0 and 1. (2 is the stopping point so it stops right after 1)
print(fruits[:2]) # start from the beginning no first number
print(fruits[1:]) # start at a number and go to the end of the list like the last part except leave 2nd number empty

# modifying lists
fruits[1]="Mango"
print(fruits)

# Adding items
fruits.append("orange") # adds item to the end
print(fruits)

fruits.insert(1, "kiwi") # inserts item and position specified
print(fruits)

# removing items
fruits.remove("apple") #remove by name not position
print(fruits)

fruits.pop() # remove last item
print(fruits)

del fruits[0] # removes item at index 0
print(fruits)

#list length
print(len(fruits))
print(len(["cohort63", True, "python", 3.1416, 2025]))


"""
create a list of 4 movies
replace the second movie with a new one
remove one movie
    option a:remove by value
    option b:remove by index
print the list 
print the lenghth

"""

movies = ["seven", "prisoners", "F1", "a few good men"]
movies[1]= "weapons"
del movies[3] # remove by index
print(movies)
print(len(movies))