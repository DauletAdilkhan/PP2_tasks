import re

s = input()
b = input()

rep = re.escape(b)
res= re.findall(rep,s)
print(len(res))

import re
