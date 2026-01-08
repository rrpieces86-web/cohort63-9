"""
Docstring for function
functions

a function is a block  of code that only  runs when it is called
we can pass date to functions with (paramaters), and they can return data as a result

def funtion_name(paramaters)
    code block (indented)
    return value # optional
"""
def my_function():
    print("this is a function")

my_function()

def other_function():
    print("this is another function")

other_function()

def hello():
    cohort = 63
    print("hello cohort#, cohort")

hello()
hello()
my_function()
hello()

def get_full_name(first_name, last_name):
    return f"hello {first_name} {last_name}" # sends back the full name as text

full_name = get_full_name("Reece", "Rollins")
print(full_name)

def greet(name=""):
    print(f"hello, {name}, welcome to class.")

greet()
greet("pam")
greet("angela")
