"""newlist = [expression for item in iterable if condition == True]"""

#Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits if x != "apple"]
print(newlist1)
#With no if statement:
newlist2 = [x for x in fruits]
print(newlist2) 

