import re
a =input()
patern =r'\b\w{3}\b'
res = re.findall(patern,a)
print(len(res))
