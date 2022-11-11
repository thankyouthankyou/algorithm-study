L = []
for i in range(5):
    L.append(sum(list(map(int, input().split()))))

print(L.index(max(L)) +1 , max(L))