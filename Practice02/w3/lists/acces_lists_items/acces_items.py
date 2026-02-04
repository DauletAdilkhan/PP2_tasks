"""Note: The first item has index 0."""
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Print the last item of the list:
print(thislist[-1])


#Return the third, fourth, and fifth item:
thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist1[2:5])

"""Note: The search will start at index 2 (included) and end at index 5 (not included)."""

#This example returns the items from the beginning to, but NOT including, "kiwi":
print(thislist1[:4])

#This example returns the items from "cherry" to the end:
print(thislist1[2:])


#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
print(thislist1[-4:-1])