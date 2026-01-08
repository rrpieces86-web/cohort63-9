"""
Docstring for sets
sets in python

a set is a built-in data structure in python used to store unique items
sets are unordered,  unindexed and do not allow duplicate values

my_set = {item1, item2, item3, ...}
"""

fruits = {"apple", "banana", "cherry"}
print(fruits)

fruits = {"apple", "banana", "apple"}
print(fruits) # duplicate "apple" is ignored

print("banana" in fruits)
# add item to set
fruits.add("orange")
print(fruits)

# add more than 1 item

fruits.update(["kiwi", "mango"])
print(fruits)

# remove item

fruits.remove("banana") #removes but error if not found
print(fruits)

fruits.discard("watermelon") #removes with no error even if not found
print(fruits)

# set operations

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) # union combines but doesnt do duplicates
print(set1.intersection(set2)) # intersection only prints duplicates
print(set1.difference(set2))

# length
print(len(set1))

# copying sets
new_set = set1.copy()
print(new_set)

#clearing sets
set1.clear()
print(set1)

