"""----------------------------Generators--------------------------------"""
###When a generator function is called, it returns a generator object, which is an iterator.


#A simple generator function:
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

"""The keyword is what makes a function a generator.yield

When is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.yield"""

#Generator that yields numbers:
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)



"""---------------------------Generators Saves Memory---------------------------------"""
#Generator for large sequences:
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))


"""----------------------------Using next() with Generators-------------------------------"""
###You can manually iterate through a generator using the next() function:
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))


"""-----------------------------Generator Expressions-------------------------------"""
###List comprehension vs generator expression:

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))




###Using a generator expression with sum:
# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

###Generate 100 Fibonacci numbers:

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))


"""---------------------------Generator Methods---------------------------------"""
###send() method allows you to send a value to the generator:


def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")


###close() method stops the generator:
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()