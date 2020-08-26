import math 

def add(x,y):
    return x + y

def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i 
    return sum 

def sin(x,N):
    sum = 0
    for n in range(N+1):
        sum += (((-1)**n) * (x**(2*n+1)))/(factorial(2*n+1))
    return sum

def divide(x,y):
    return x/y 

def multi(x,y):
    return x*y 

def minus(x,y):
    return y-x 

    