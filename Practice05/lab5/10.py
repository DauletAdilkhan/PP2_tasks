import re
a =input()
patern =r'dog|cat'
res = re.search(patern,a)
if res:
    print("Yes")
else:
    print("No")