L = []
a, b = map(int, input().split())
for i in range(1000):
  for j in range(i): 
    L.append(i)
    
print(sum(L[a-1:b]))
