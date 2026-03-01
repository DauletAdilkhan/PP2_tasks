import re 

def fi(n):
    patern = r'...'
    res = re.match(patern, n)
    if len(n)==3:
        return True


a= list(map(str,input().split()))
cnt= 0
for i in a:
    if fi(i):
        cnt+=1

print(cnt)
