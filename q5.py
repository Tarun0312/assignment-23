# 5. Create a generator to produce first n terms of Fibonacci series

from re import A


def genFib(n):
    a,b=0,1
    while(n):
        yield a 
        a,b=b,a+b
        n-=1
for e in genFib(int(input("Enter a number: "))):
    print(e,end=' ')