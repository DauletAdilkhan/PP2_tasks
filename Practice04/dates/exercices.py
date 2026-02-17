## 1:Write a Python program to subtract five days from current date.


from datetime import timedelta,datetime,date

x = datetime.now()
print("5days ago:",(x-timedelta(days=5)).strftime("%x"))
print("today:",x.strftime("%x"))


## 2:Write a Python program to print yesterday, today, tomorrow.

from datetime import timedelta,datetime

x = datetime.now()
print("yesterday:",(x-timedelta(days=1)).strftime("%x"))
print("today:",x.strftime("%x"))
print("tomorrow:",(x+timedelta(days=1)).strftime("%x"))


## 3:Write a Python program to drop microseconds from datetime.

from datetime import timedelta,datetime

x = datetime.now()
print("with microseconds:",x)
nm=x.replace(microsecond=0)
print("without microseconds:",nm)


## 4:Write a Python program to calculate two date difference in seconds.
from datetime import timedelta,datetime
import math
x=input()
n=input()
firstd= datetime.strptime(x,"%Y-%m-%d")
secondd= datetime.strptime(n,"%Y-%m-%d")
print(int(abs((firstd-secondd).total_seconds())),"seconds")