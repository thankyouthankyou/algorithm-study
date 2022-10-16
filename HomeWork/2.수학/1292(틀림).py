L = []
a, b = map(int, input().split())

for i in range(1000):
    if i==7:
        break
    for j in range(i):
        L.append(i)
    
print(sum(L[a-1:b]))
# print(L[999])