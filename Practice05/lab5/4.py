import re
a = str(input())
res = re.findall("\d", a)
if res:
    print(*res,end=" ")
else:
    print()