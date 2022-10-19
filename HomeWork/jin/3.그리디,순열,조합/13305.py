n=int(input())
dis=list(map(int,input().split()))
node=list(map(int,input().split()))

node[-1]=1000000001
dis.append(0)

rs=dis[0]*node[0]
acc_dis=0
minV=node[0]

for i in range(1,n):
    if minV<=node[i]:
        acc_dis+=dis[i]
    else:
        rs+=acc_dis*minV
        acc_dis=dis[i]
        minV=node[i]
rs+=acc_dis*minV
print(rs)