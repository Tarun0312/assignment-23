# 8. Create an endless iterator using generator method to produce Prime numbers

def genPrime():
    i=2
    while(i):
        j=2
        while(j<=i**0.5):
            if(i%j==0):
                break
            j+=1
        else:
            yield i             
        i+=1

it=genPrime()
l=[]
while(True):
    a=input("Do you want to generate another prime number: ")  
    if(a=='y'):
        x=next(it)
        l.append(x)
        print(x)
    else:
        print(l)
        break    
