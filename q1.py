# 1. Use iter and next method to access all the elements of a given set using while loop

s1={e*e for e in range(1,11)}

it=iter(s1)

i=0
while(i<len(s1)):
    print(next(it),end=' ')
    i+=1