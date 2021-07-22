#!/usr/bin/python
 
def countBits(n):
    count = 0
    while n > 0 :
        if(n&1) == 1:
            count = count+1
        n>>=1
    return count
    
print (countBits(1234))
