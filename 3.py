from datetime import datetime 
a=[]
for i in range(4):
    b= input()
    a.append(b)
for i in a:
    i= datetime.strptime(i,"%Y-%m-%d")
s=a[1]-a[0]
print(s.days)
#sum = (a[0]-a[1])+(a[1]-a[2])+(a[2]-a[3])+(a[3]-a[4])
#print(sum.days)
