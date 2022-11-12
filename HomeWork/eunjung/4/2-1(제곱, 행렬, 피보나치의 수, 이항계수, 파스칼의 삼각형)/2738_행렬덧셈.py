N, M = map(int, input().split())
a=[]
b=[]

for i in range(N):
  a.append(list(map(int, input().split())))
for i in range(N):
  b.append(list(map(int, input().split())))

for i in range(N):
  for j in range(M):
    print(a[i][j]+b[i][j], end=" ")
    if j == M-1 :
      print()