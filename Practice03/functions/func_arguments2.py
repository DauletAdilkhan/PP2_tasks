"""--------------------------Return Values----------------------------"""
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


"""-----------------------------Returning Different Data Types------------------------------"""
#A function that returns a list:
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


#A function that returns a tuple:
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

"""----------------------------Positional-Only Arguments-----------------------------"""
def my_function(name, /):
  print("Hello", name)

my_function("Emil")



def my_function(name):
  print("Hello", name)

my_function(name = "Emil")


"""--------------------------Keyword-Only Arguments------------------------------"""
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")


def my_function(name):
  print("Hello", name)

my_function("Emil")


"""------------------------------Combining Positional-Only and Keyword-Only----------------------------"""
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


"""----------------asik loh---------------------"""