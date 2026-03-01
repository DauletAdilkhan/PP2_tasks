import re
a = str(input())
patern=r'^[a-zA-Z].*[0-9]'
res = re.search(patern, a)
if res is not None:
    print("Yes")
else:
    print("No")