# 7. Create an endless iterator using generator method to produce terms of Fibonacci
# series

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

it=fib()
fib_list=[]
while(True):
    ans=input("Do u want to generate another element: ")
    if(ans=='y'):
        c=next(it)
        fib_list.append(c)
        print(c)   
    else:
        print(fib_list)
        break 