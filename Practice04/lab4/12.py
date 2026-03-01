import json
def comp(a,b,path=""):
    diffs=[]
    if isinstance(a,dict)and isinstance(b,dict):
        ak=set(a.keys())|set(b.keys())
        for key in sorted(ak):
            cur=f"{path}.{key}"if path else key

            if key not in a:
                b = json.dumps(b[key])
                diffs.append(f"{cur}: <missing> -> {b}")
            elif key not in b:
                a = json.dumps(a[key])
                diffs.append(f"{cur} : {a} -> <missing>")
            else:
                diffs.extend(comp(a[key],b[key],cur))

    elif a !=b:
        a = json.dumps(a)
        b = json.dumps(b)
        diffs.append(f"{path} : {a} -> {b}")
    return diffs

A= json.loads(input())
B=json.loads(input())
C= comp(A,B)
print()
if C:
    for i in sorted(C):
        print(i)
else:
    print("No differences")