import re
a =input()
patern =r'[A-Z]'
res = re.findall(patern,a)
print(len(res))