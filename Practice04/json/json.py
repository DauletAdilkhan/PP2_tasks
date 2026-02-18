"""--------------------------JSON in Python---------------------------------"""
###Import the json module:
import json

"""---------------------------Parse JSON - Convert from JSON to Python------------------------------"""
##If you have a JSON string, you can parse it by using the json.loads() method.
###Convert from JSON to Python:


import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



"""---------------------------Convert from Python to JSON-----------------------------"""
##If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
###Convert from Python to JSON:


import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


"""---------------------------------------------------------------"""
###Convert Python objects into JSON strings, and print the values:
import json

print(json.dumps({"name": "John", "age": 30}))  #dict
print(json.dumps(["apple", "bananas"]))         #list
print(json.dumps(("apple", "bananas")))         #tuple
print(json.dumps("hello"))                      #str
print(json.dumps(42))                           #int
print(json.dumps(31.76))                        #float
print(json.dumps(True))                         #True
print(json.dumps(False))                        #False
print(json.dumps(None))                         #None

"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python         JSON
dict-----------Object
list-----------Array
tuple----------Array
str------------String
int------------Number
float----------Number
True-----------true
False----------false
None-----------null
"""

###Convert a Python object containing all the legal data types:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

"""----------------------------Format the Result---------------------------------"""
###Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

###Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))


"""------------------------------Order the Result-----------------------------"""
###Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)