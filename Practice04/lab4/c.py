from datetime import timedelta,datetime
y=input()
a=input()
x = datetime.strptime(y,"%Y-%m-%d")
b = datetime.strptime(a,"%Y-%m-%d")
print(int(abs(x-b).total_seconds())//(60*3600))

print()
