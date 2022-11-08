from collections import deque

n, k = map(int,input().split())
inp = list(map(int,input().split()))

li = deque([i for i in range(1,n+1)])
cnt=0
n = len(li)
for i in inp:
    ind = li.index(i)
    if ind<=n-ind:
        cnt+=ind
        for _ in range(ind):
            li.append(li.popleft())
        n-=1
        li.popleft()
    else: #역방향
        cnt+=n-ind
        for _ in range(n-ind):
            li.appendleft(li.pop())
        n-=1
        li.popleft()
print(cnt)