"""
Docstring for tuples

tuples in python

a tuple is a built-in data structure in python, like a list
tuples can store multiple items, but they are immutable.

my_tuple = (item1, item2, item3, ...)

"""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[2])

# length
print(len(my_tuple))

# single item in tuples
single = ("apple")
print(type(single))

print(my_tuple[0:2])

# nested tuples
tuple1 =("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)
# turning a tuple into  list
temp_list = list(my_tuple)
print(temp_list)

"""
mini- challenge

1. Create a tuple called travel_bag with at least 5 items
shirt, socks, pants, jacket, shoes

2. print the second and 4th items.
3. make a new tuple called essential with 3 items
"""

travel_bag = ("shirt", "socks", "pants", "jacket", "shoes")
print(travel_bag)
print(travel_bag[1])
print(travel_bag[3])
essentials = ("books", "laptop", "notebooks")
print(essentials)


