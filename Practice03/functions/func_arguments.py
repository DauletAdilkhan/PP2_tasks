#A function with one argument:
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

"""From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called."""
#example:
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument



#This function expects 2 arguments, and gets 2 arguments::
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


"""-----------------------------Default Parameter Values-----------------------------"""
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Default value for country parameter:
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


"""------------------------------Keyword Arguments------------------------------"""

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#Switching the order changes the result:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")



"""------------------------------Mixing Positional and Keyword Arguments--------------------------------"""

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

"""------------------------------Passing Different Data Types-----------------------------"""

#Sending a list as an argument:
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Sending a dictionary as an argument:
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
