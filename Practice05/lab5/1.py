import re
a = str(input())
patern= "Hello"
res = re.match(patern, a)
if res is not None:
    print("Yes")
else:
    print("No")