# 왜 이런 점화식..?
N=int(input())
L=[0, 1, 2, 4]
for i in range(4, 12):
    L.append(L[i-1]+L[i-2]+L[i-3])

for i in range(N):
    n=int(input())
    print(L[n])
