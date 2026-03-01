def a(n,m):
    for i in range(n, m + 1):
        yield i**2

n,m = map(int,input().split())
print(*a(n,m))

def a(n):
    for i in range(n+1):
        if i%2==0:
           yield i
n= int(input())
print(*a(n)) 







n=int(input())
def a(n):
    for i in range(0,n+1,2):
            yield i
for i in range(n/2):
    print(next(a(n)))