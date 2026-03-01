import re
a =input()
pattern = re.compile(r'^\d*$')

if pattern.match(a):
    print("Match")
else:
    print("No match")