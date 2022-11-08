from collections import deque

n, k = map(int,input().split())
li = deque([i for i in range(1,n+1)])
rs=[]

while len(li):
    for _ in range(k-1):
        li.append(li.popleft())
    rs.append(li.popleft())
  
print('<',end='')
for i in rs[:-1]:
    print(i,end=', ')
print(rs[-1],'>',sep='')