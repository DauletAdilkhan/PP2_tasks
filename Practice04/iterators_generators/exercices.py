## 1:Create a generator that generates the squares of numbers up to some number N.

n=int(input())
sq=(x*x for x in range(n))
print(sq)
print(list(sq))


## 2:Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

n2= int(input())
en=(x for x in range(n2) if x%2==0 )
print(*en,sep=", ")

## 3:Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def div_six(n):
    for x in range(0,n):
        if x%4==0 and x%3==0:
            yield x

n3= int(input())
dv= div_six(n3)
print(*dv, sep=", ")


## 4:Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares(a,b):
    for x in range(a,b):
        yield x*x

a=int(input())
b=int(input())
for _ in squares(a,b):
    print(_, end=", ")


## 5:Implement a generator that returns all numbers from (n) down to 0.
def all_num(start,end,step=-1):
    while(start>end):
        yield start
        start+=step

n5=int(input())
for x in all_num(n5,-1):
    print(x,end=" ")
