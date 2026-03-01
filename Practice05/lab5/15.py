import re

def db(match):
    d=match.group()
    return d*2

a=input()
res=re.sub(r'\d',db,a)

print(res)

