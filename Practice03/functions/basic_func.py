#In Python, a function is defined using the def keyword, followed by a function name and parentheses:"""
def my_function():
    print("Hello from a function")

#To call a function, write its name followed by parentheses:"""
def my_function1():
  print("Hello from a function")

my_function1()

#You can call the same function multiple times:
def my_function2():
  print("Hello from a function")

my_function2()
my_function2()
my_function2()

#Valid functions names:
"""
calculate_sum()
_private_function()
myFunction89()
"""

"""------------------------------------------------------"""
#Without functions - repetitive code:
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

#With functions - reusable code:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

"""----------------return values----------------------"""
#A function that returns a value:
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


#Using the return value directly:
def get_greeting():
  return "Hello from a function"

print(get_greeting())


"""----------------------pass---------------------------"""
def my_function():
  pass
