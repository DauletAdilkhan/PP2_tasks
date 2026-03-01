import json
import re
def gv(d,q):
    parts = re.split(r'\.|\[|\]',q)

    parts = [p for p in parts if p]

    cur = d
    pe=True

    for part in parts:
        if part == None:
            return 
        if part.isdigit():
            idx = int(part)
            if isinstance(cur,list) and 0<=idx < len(cur):
                cur = cur[idx]
            else:
                pe = False
                break
        else:
            if isinstance(cur,dict) and part in cur:
                cur = cur[part]
            else:
                pe = False
                break
    if not pe:
        return None,False
    else:
        return cur, True







a=json.loads(input())
n=int(input())
q=[]
for i in range(n):
    inp= input()
    q.append(inp)
for i in q: 
    res,ex=gv(a,i)
    if not ex:
        print("NOT_FOUND")
    else:
        print(json.dumps(res,separators=(',',':')))
