# dictionaries in python

"""
A dictionary is a built-in data structure in python used to store data in key:value pairs.
dictionaries are mutable, ordered, keys must be unique
option 1
my_variable = {"key1": value1, "key2": value2, ....}
option 2
my_variable = {
    "key1": value1,
    "key2": value2,
    ...
}
"""
# creating a dictionary
student = {
    "name": "John",
    "age": 68, 
    "major": "Computer Science"
}

print(student)

new_student = {
    "name": "Pam",
    "age": 31,
    "name": "Angela" # if you use the same key twice, the lasgt value will overwrite the previous one.
}

print(new_student)

# Accessing items
print(student["name"])
print(student["age"])
print(student["major"])

#adding new items
student["graduation_year"] = 2025
print(student)

# changing values
student["age"] = 20
print(student)

# removing items
student.pop("major") #remove by key
print(student)

del student["name"] # removes specific key
print(student)

# dictionary length

print(student)
print(len(student))

# clearing dictionaries
student.clear()
print(student)

students_group = {
    "student_one":{
        "name": "bruce",
        "age": 20
    },
    "student_two": {
        "name": "peter",
        "age": 89
    }
}

print(students_group)
print(students_group["student_two"]["name"])


"""
create a dictionary called song with keys: "title", "artist", "duration"
print the title value
add a new key to "album".
update "duration" to a new value
remove "album"
print the dictionary length
"""

album = {
    "title": "sappy",
    "artist": "nirvana",
    "duration": 4
    }
print(album)
album["rating"] = 10
print(album)
album["duration"] = 5
print(album)
album.clear()
print(album)