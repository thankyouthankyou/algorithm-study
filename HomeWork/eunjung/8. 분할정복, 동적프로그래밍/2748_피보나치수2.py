N = int(input())
L=[0, 1]

for i in range(N-1):
  L.append(L[i]+L[i+1])

print(L[-1])