# Python Basics - Sesssion#1

print("Hello World from Python") # no seimicolons needed at the end of lines
print(2) # printing a number
print(5 + 3) # printing the result of a math operation

print("Cohort#63 Welcome")


# Shortcuts
# windows: ctrol + s
#macos: command + s

"""
this is a multi-line comment (docstring)
triple quotes let you write longer explanations
"""


#------variables and contatenation-------
name = "angela"
age = 28
print(name) # prints the variable value

print("My name is " + name + " and i am " + str(age) + " years old.")

first_name = "Micheal"
middle_name = "John"
last_name = "Scott"
age = 46

print("My name is " + first_name + " " + middle_name + " " + last_name + " and I am " + str(age) + " year old.")


# ------ F-string (cleaner way to format strings)------
print(f"hello")
print(f"My name is {first_name} {middle_name} {last_name} and I am {age} years old")

# multi-line f-string
print(f"""
      My name is {first_name} {middle_name} {last_name}
      and I am {age} years old
      """)

my_first_name = "Reece"
my_last_name = "Rollins"
my_age = 39
my_favorite_technology = "my phone"
my_city = "D.C."
my_hobbie = "skateboarding"
my_technology = "python"
print(f"""
Hello my name is {my_first_name} {my_last_name} 
and I am {my_age} years old
my favorite code is {my_technology}
and I love {my_hobbie} around {my_city} while recording on {my_favorite_technology}
""")

# type function

print(type("Peter"))
print(type(last_name))
print(type(True))
print(type(1234))


# -------  input function ------
user_name = input("Enter your name: ")
print(f"Hello {user_name}")

user_age = int(input("Enter your age: "))
print(f"You are {user_age - 1} years old.")
