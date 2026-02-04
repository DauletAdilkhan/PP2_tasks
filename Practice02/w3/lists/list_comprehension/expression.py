#Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x.upper() for x in fruits]
print(newlist1)

#Set all values in the new list to 'hello':
newlist2 = ['hello' for x in fruits]
print(newlist2)

#Return "orange" instead of "banana":
newlist3 = [x if x != "banana" else "orange" for x in fruits]
print(newlist3)


