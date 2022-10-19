n=int(input())
li = list(map(int,input().split()))
li.sort()
rs=0
for i in range(n):
    rs+=li[i]*(n-i)
print(rs)