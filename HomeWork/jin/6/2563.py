drawing = [[0]*101 for _ in range(101)]
cnt=0

n = int(input())
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            drawing[i][j]=1

for i in drawing:
    cnt+=i.count(1)
print(cnt)