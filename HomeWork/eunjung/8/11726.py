L=[1,2]
N = int(input())
for i in range(2,N):
    L.append(L[i-2]+L[i-1])
print(L[N-1]%10007)