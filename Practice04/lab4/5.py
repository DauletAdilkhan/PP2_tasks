def cntdwn(n):
    for i in range(n,-1,-1):
        yield i
n = int(input())
for _ in cntdwn(n):
    print(_)