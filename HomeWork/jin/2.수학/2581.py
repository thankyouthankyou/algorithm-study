def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True


a = int(input())
b = int(input())

sum = 0
minV = b+1
for i in range(a, b+1):
    if isPrime(i):
        sum += i
        minV = min(minV, i)

if sum == 0:
    print(-1)
else:
    print(sum)
    print(minV)
