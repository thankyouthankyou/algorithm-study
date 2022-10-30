N = int(input())
L=[]
for i in range(N):
    x, y = map(int, input().split())
    L.append((x, y))
#y로 오름차순 정렬하고, y가 같은 경우 x로 오름차순 정렬
L.sort(key=lambda x:(x[1], x[0]))
y = L[0][1]
C = 1
for i in range(1, N):
    if (L[i][0] >= y) and (L[i][1] >= y):
        C += 1
        y = L[i][1]
print(C)