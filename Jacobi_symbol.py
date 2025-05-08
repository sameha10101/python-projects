"""
Jacobi symbol
"""

def Jacobi_symbol(a,n):
    if n%2==0 or n<1:
        raise ValueError('the second argument must be positive and odd.')
    if n==1: #if n=1, then (a/n)=1 if a is nonzero, and (0/1)=0
        if a==0:
            return 0
        if a != 0:
            
            return 1
    if (n>1 and n%2==1):
        if a==0:
            return 0
        t=1
        if a<0: #get rid of negative sign.
            a=-a
            if n%4==3:
                t=-t
        while a>0:
            if a%2==0: #if a even, divide by 2 & change sign accordingly.
                a=a/2
                if (n%8==3 or n%8==5):
                    t=-t
            if (a%2==1 and a>1):
                a, n = n,a
                if (a%4==3 and n%4==3):
                    t=-t
                if a%n==0:
                    return 0
                if a%n !=0:
                    a=a%n
            if a==1:
                return t