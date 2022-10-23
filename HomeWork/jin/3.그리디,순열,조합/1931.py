n=int(input())
li=[[0,0]]
for _ in range(n):
    inp = list(map(int,input().split()))
    li.append(inp)
li.sort(key=lambda x:(x[1],x[0]))
cnt=0
maxV=0
# print(li)
for i in range(1,len(li)):
    if li[i][0]>=maxV:
        maxV=li[i][1]
        cnt+=1
print(cnt)