"""Solovay Straasen primality testing"""

import random

#first define a function to find gcd:
    
def gcd(a,b):
    #convert numbers nonnegative:
    a= int(abs(a))
    b= int(abs(b))
    if not a*b: #if a or b is zero, return the other without the sign
        return max(a,b)
    while not not a*b: #keep reducing using remainders
        return gcd(b, a%b)
    
# modular exponentiation: basic workable code
# more efficient if you do successive squaring writing b in binary.

def modular_exponential(a,b,n):
    if a==0:
        return 0
    if b<=0:
        raise ValueError('the exponent must be positive.')
    power=0
    exponential_iterant=1
    while power<len(range(b)):
        exponential_iterant = (exponential_iterant*a)%n
        power=power+1
    if exponential_iterant> int(n/2):
        exponential_iterant= exponential_iterant- n
    return exponential_iterant



# we next require Jacobi symbol. 

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

# We will now give the code for probable prime checker:

#for x in range(1,60,2):
#    print(f"Jacobi(13, {x})={Jacobi_symbol(13,x)}")

'''This program fails to check for very large numbers N since
 the modular expoential code that I've used
 will have to do N/2 many multiplications.
Instead use a faster algorithm for modular exponentiation.
But this works well for smaller numbers.'''
    
    
def Solovay_Straasen(N,k):
    if N==1:
        return "1 is not a prime."
    if N==2:
        return "2 is a prime."
    if (N%2==0 and N>2) or N%5==0:
        return f"{N} is not a prime."
    else:
        rand_nums=[random.randrange(3,N,2) for x in range(k)]
        index=0
        while index<k:
            if gcd(rand_nums[index], N) != 1:
                return f"{N} is not a prime, as it shares a factor with {rand_nums[index]}"
            else:
                if modular_exponential(rand_nums[index], int((N-1)/2), N) != Jacobi_symbol(rand_nums[index], N):
                    return f"{N} is not a prime"
                else:
                    index=index+1
        return f"{N} is probably a prime with probability of 1-(1/2)^{k}"
    

random_odds=[random.randrange(1,1000,5) for x in range(100)]
for N in random_odds:
    print(Solovay_Straasen(N, 5))
