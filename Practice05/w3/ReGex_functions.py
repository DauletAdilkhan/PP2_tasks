"""---------------------------------------The findall() Function------------------------------------------------"""
###The findall() function returns a list containing all matches.
#Print a list of all matches:
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

###If no matches are found, an empty list is returned:
#Return an empty list if no match was found:
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)



"""-----------------------------------------The search() Function----------------------------------------------"""
###The search() function searches the string for a match, and returns a Match object if there is a match.
###If there is more than one match, only the first occurrence of the match will be returned:
#Search for the first white-space character in the string:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

###If no matches are found, the value None is returned:
#Make a search that returns no match:
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



"""--------------------------------------------The split() Function-------------------------------------------"""
###The split() function returns a list where the string has been split at each match:
#Split at each white-space character:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

###You can control the number of occurrences by specifying the maxsplit parameter:
#Split the string only at the first occurrence:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)



"""--------------------------------------------The sub() Function-------------------------------------------"""
###The sub() function replaces the matches with the text of your choice:
#Replace every white-space character with the number 9:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)



###You can control the number of replacements by specifying the count parameter:
#Replace the first 2 occurrences:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
