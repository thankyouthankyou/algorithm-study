M= int(input())
N= int(input())

L = []

for n in range(M, N+1):
    if n == 1:
        continue
    if n == 2 or n == 3:
        L.append(n)
    else:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                break
            if i == int(n/2):
                L.append(n)

if len(L) == 0:
    print(-1)
else:
    print(sum(L))
    print(min(L))