N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
C = 0
for i in range(N):
    C += (i+1) * L[i]
print(C)
