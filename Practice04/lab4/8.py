def ip(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime(n):
    for i in range(2,n+1):
        if ip(i):
            yield i



a = prime(int(input()))
print(*a)


