#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


"""Nested Loops"""
#Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


"""The pass Statement"""
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass