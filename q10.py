# 10. Define a function which calculates HCF of two numbers. Define and apply a
# decorator to check whether two given numbers are co-prime or not.

def decor_HCF(HCF_func):
    def checkCoprime(a,b):
        i=2
        g=a if(a>b) else b
        while(i<=g**0.5):
            if(a%i==0 or b%i==0):
                print("(%d,%d) are not co-prime"%(a,b))
                break
            i+=1
        else:
            print("(%d,%d) are co-prime numbers"%(a,b))
        return HCF_func(a,b)
    return checkCoprime            


@decor_HCF
def HCF(a,b):
    H=a if(a<b) else b      
    while(H>=1):     
        if(a%H==0 and b%H==0):
            return H
        H-=1

print(HCF(int(input("Enter two numbers: ")),int(input())))