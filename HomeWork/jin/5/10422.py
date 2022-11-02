from math import factorial

def catal(n):
    if n%2==1:
        return 0
    else:
        k=n//2
        return (factorial(n)//(factorial(k+1)*factorial(k)))% 1000000007

n = int(input())

for _ in range(n):
    inp = int(input())
    print(catal(inp))