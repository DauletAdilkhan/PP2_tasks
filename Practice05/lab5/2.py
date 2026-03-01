import re
a = str(input())
patern= str(input())
res = re.search(patern, a)
if res is not None:
    print("Yes")
else:
    print("No")