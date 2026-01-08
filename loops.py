"""
Docstring for loops
loops

A for loop in python is a control structure that lets you repeat a block of code for each item in sequence
such as (list, string, tuple, dictionary or a range of numbers)

for variable in sequence:
    -code block runs for eacch item in the sequence
"""

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


print("----------------")


for letter in "Reece":
    print(letter)

print("---------------------")

for number in range(5):
    print(number) # prints 0,1,2,3,4 because range() only includes numbers less than the stop value.

print("---------------------")

for number in range(2, 6):
    print(number)

print("---------------------")

for number in range(0, 10, 2):
    print(number)

print("--------------------")



"""
mini-challenge

1. ask the user to enter a number and store it in a variable called num
2. use a for loop with range(1,11) to repeat 10 times (from 1 to 10)
3. inside the loop, multiply num by the current loop value
"""

num = int(input("pick a number: "))

for number in range(1,11):
    total = number * num
    print(f"{number} * {num} = {total}")

"""
While loops

a while loop repeats a block of code as long as a condition is true

while condition:
    -code block runs as long as condition is true

"""


count = 1

while count <=5:
    print("count is ", count)
    count += 1

number = 0

while True: # infinite loop
    print(number)
    number += 1
    if number ==22:
        break # stop the loop when number reaches 22