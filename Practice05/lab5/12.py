import re
a =input()
patern =r'\d{2,}'
res = re.findall(patern,a)
print(*res)