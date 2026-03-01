import re
a = str(input())
patern= str(input())
res = re.findall(patern, a)
print(len(res))