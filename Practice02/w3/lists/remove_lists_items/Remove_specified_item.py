"""Remove()"""
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove the first occurrence of "banana":
thislist1 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist1.remove("banana")
print(thislist1)

"""POP()"""
#Remove the second item:
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop(1)
print(thislist2)

#Remove the last item:
thislist3 = ["apple", "banana", "cherry"]
thislist3.pop()
print(thislist3)


"""del"""
#Remove the first item:
thislist4 = ["apple", "banana", "cherry"]
del thislist4[0]
print(thislist4)

#Delete the entire list:
thislist5 = ["apple", "banana", "cherry"]
del thislist5

"""clear()"""
#Clear the list content:
thislist6 = ["apple", "banana", "cherry"]
thislist6.clear()
print(thislist6)

