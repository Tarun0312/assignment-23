# 2. Create a generator to produce first n odd natural numbers

from re import A


def generatorOddN(n):
    a=1
    while(n):
        yield a
        a+=2
        n-=1

for e in generatorOddN(int(input("Enter a number: "))):
    print(e,end=' ')