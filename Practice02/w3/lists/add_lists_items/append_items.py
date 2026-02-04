thislist = ["apple", "banana", "cherry"]
"""Append"""
#Using the append() method to append an item:
thislist.append("orange")
print(thislist)

"""Insert"""
#Insert an item as the second position:
thislist.insert(1, "orange")
print(thislist)

"""Extend"""
#Add the elements of tropical to thislist:
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""Add any iterable"""
#Add elements of a tuple to a list:
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)