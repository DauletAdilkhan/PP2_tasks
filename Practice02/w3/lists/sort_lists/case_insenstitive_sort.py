#Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Perform a case-insensitive sort of the list:
thislist.sort(key = str.lower)
print(thislist)

