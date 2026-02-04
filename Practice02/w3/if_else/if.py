"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

#if statement
a = 33
b = 200
if b > a:
    print("b is greater than a")

#Checking if a number is positive:
number = 15
if number > 0:
  print("The number is positive")

#Multiple statements in an if block:
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#Using a boolean variable:
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

"""Python can evaluate many types of values as True or False in an if statement.

Zero (0), empty strings (""), None, and empty collections are treated as False.
Everything else is treated as True.

This includes positive numbers (5), negative numbers (-3),
and any non-empty string (even "False" is treated as True because it's a non-empty string)."""