a,b=map(int,input().split())
li1 = [list(map(int,input().split())) for _ in range(a)]
c,d=map(int,input().split())
li2 = [list(map(int,input().split())) for _ in range(c)]
li3 = [[0]*d for _ in range(a)]
for i in range(a):
    for j in range(d):
        sum=0
        for k in range(b):
            sum+=li1[i][k]*li2[k][j]
        li3[i][j]=sum
    print(*li3[i])