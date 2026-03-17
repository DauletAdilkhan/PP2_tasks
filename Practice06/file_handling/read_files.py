"""------------------------------Open a File on the Server------------------------------"""
#Assume we have the following file, located in the same folder as Python:

"""
-------demofile.txt--------

Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""

#To open the file, use the built-in open() function.

#The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt")
print(f.read())



#Open a file on a different location:
f = open("D:\\myfiles\welcome.txt")
print(f.read())


"""------------------------------Using the with statement-------------------------------"""
###You can also use the with statement when opening a file:
#Using the with keyword:
with open("demofile.txt") as f:
  print(f.read())

"""-------------------------------Close Files------------------------------"""
###It is a good practice to always close the file when you are done with it.

###If you are not using the with statement, you must write a close statement in order to close the file:

#Close the file when you are finished with it:
f = open("demofile.txt")
print(f.readline())
f.close()


"""-------------------------------Read Only Parts of the File------------------------------"""
###By default the read() method returns the whole text, but you can also specify how many characters you want to return:
#Return the 5 first characters of the file:
with open("demofile.txt") as f:
  print(f.read(5))


"""------------------------------Read Lines-------------------------------"""
###You can return one line by using the readline() method:
#Read one line of the file:
with open("demofile.txt") as f:
  print(f.readline())

###By calling readline() two times, you can read the two first lines:
#Read two lines of the file:
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())


###By looping through the lines of the file, you can read the whole file, line by line:
#Loop through the file line by line:
with open("demofile.txt") as f:
  for x in f:
    print(x)