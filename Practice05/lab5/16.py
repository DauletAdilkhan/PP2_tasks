import re
a= input()
patern = r'^Name:\s*([^,]+),\s*Age:\s*(\S+)'
match = re.search(patern,a)
if match:
    name = match.group(1)
    age = match.group(2)
    print(f"{name} {age}")