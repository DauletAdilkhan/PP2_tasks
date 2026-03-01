import re
a = input().strip()
patern=r'\S+@\S+\.\S+'
res = re.search(patern, a)
if res:
    print(res.group())
else:
    print("No email")