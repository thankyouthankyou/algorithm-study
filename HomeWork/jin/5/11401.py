# from math import factorial
import sys
input = sys.stdin.readline

def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % 1000000007
    return n

def exp(a, b):
    if b==0:
        return 1
    elif b==1:
        return a
    c = exp(a,b//2)
    if b%2==0:
        return c*c%1000000007
    else:
        return c*c*a%1000000007
    
n, k = map(int, input().split())
p = 1000000007
print(factorial(n)*exp(factorial(k)*factorial(n-k),1000000005)%1000000007)