# 3. Create a generator to produce first n even natural numbers

from re import A


def generatorEvenN(n):
    a=2
    while(n):
        yield a 
        a+=2
        n-=1

for e in generatorEvenN(int(input("Enter a number"))):
    print(e,end=' ')