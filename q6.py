# 6. Create a generator to produce first n prime numbers


def genPrime(n):
        count=0
        p=2
        while(p):
            i=2
            while(i<=p**0.5):
                if(p%i==0):
                    break
                i+=1
            else:
                yield p
                count+=1
            if(count==n):
                break         
            p+=1


for e in genPrime(int(input("Enter a number: "))):
    print(e,end=' ')