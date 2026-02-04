"""copy()"""
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

"""list()"""
#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

""" : """
#Make a copy of a list with the list slicing method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)