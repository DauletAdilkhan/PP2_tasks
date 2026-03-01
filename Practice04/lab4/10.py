def lc(n,k):
    for _ in range(k):
        for i in n:
            yield str(i)


a= input().split()
k = int(input())

print(*lc(a,k))