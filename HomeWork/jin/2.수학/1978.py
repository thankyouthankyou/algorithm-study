n = int(input())
li = list(map(int, input().split()))


def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True


cnt = 0
for i in li:
    if isPrime(i):
        cnt += 1
print(cnt)
