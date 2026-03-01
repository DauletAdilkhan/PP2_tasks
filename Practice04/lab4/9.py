import math
def pw(a):
    for i in range(0,a+1):
        yield int(math.pow(2,i))

n =pw(int(input()))
print(*n)

