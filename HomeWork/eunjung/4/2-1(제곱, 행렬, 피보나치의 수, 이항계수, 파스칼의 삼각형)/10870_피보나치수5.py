L = [0, 1]

n = int(input())

for i in range(2, n+1):
    L.append(L[i-2] + L[i-1])

print(L[n])