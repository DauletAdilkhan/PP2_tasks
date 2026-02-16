"""--------------------------Add the __init__() Function-------------------------------"""
#Add the __init__() function to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    """add properties etc"""
###To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()


"""-----------------------Add Methods------------------------------"""
###Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

