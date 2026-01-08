"""
Docstring for if-else
if-else statement

an if-else statement in python is a conditional control structure that lets you decide which block of ccode to run depending on wheter a condition is true or false

if block runs only if the conndition evalutates are true
if the condition is fale the else block runs instead
you can also add elif (else-if) blocks to check multiple conditionns in sequence

if condition:
    - code block runis if condition is true
elif another_condition:
    - code block runs if the first conditions is false and this condition is true
else:
    -code block runs if none of the above conditions are true

(must you colon)
"""

x = 21

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# nested if statements
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# combining conditions
age =18

if age >=18 and age<=21:
    print("you are betweeen 18 and 21 years old")

username = "john123"

if username == "peter321":
    print("you are peter")

"""
mini-challenge

1. ask the user to enter a number from 0-100 and store in a variable called "score"
2. if the score is under 90 or above, print "grade: A"
3. if the scorre is between 80-89 print "grade b"
4. if the score is between 70-79, print "Grade C
5. otherwise print "grade f"
"""

grade = int(input("enter the grade: "))

if grade >= 90 and grade<= 100:
    print("grade is an A")
elif grade >=80 and grade<=89:
    print("grade: B")
elif grade >=79 and grade<=79:
    print("grade: C")
else:
    print("grade: F")


"""
mini- challenge

1. ask the user to enter today's temperature in fahrenheit and store it in a variable called temperature
2. use the if-else statements to classify the temperature:
    if temperature >= 86, print "its hot outside!"
    if temperatue is >=68 and temperate is < 86 pribt " the weather is nice"
    if temperatue is >=50 and teperature <68, print "its a bit chilly"
    otherwise print "its cold!"
"""

temp = int(input("enter the temperature: "))

if temp >= 86:
    print("It's hot outside!!")
elif temp >=68 and temp < 86:
    print("The weather is nice")
elif temp >=50 and temp < 68:
    print("It's a bit chilly")
else:
    print("It's cold!!")