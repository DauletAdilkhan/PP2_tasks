import re
a =input()
patern =r'\w+'
res = re.findall(patern,a)
print(len(res))