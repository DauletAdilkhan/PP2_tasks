import re
a =input()
pattern = re.compile(r'\b\w+\b')

res = re.findall(pattern,a)
print(len(res))