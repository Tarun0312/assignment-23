# 4. Create a generator to produce squares of first N natural numbers

from re import A


def generatorSquareN(n):
    a=1
    while(n):
        yield a*a 
        a+=1
        n-=1

for e in generatorSquareN(int(input("Enter a number: "))):
    print(e,end=' ')