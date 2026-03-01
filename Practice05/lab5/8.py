import re
a =input()
patern = input()
res = re.split(patern,a)
print(','.join(res))