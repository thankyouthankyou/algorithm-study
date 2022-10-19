a,b=map(int,input().split())
n=int(input())
numA=list(map(int,input().split()))
rs=0
for i in range(n):
    rs+=numA[n-i-1]*a**i
rs2=[]
while rs:
    rs2.append(rs%b)
    rs//=b
rs2.reverse()
print(*rs2)
