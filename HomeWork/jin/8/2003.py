n, m = map(int,input().split())
li = list(map(int,input().split()))

start, end = 0, 1
cnt = 0
while start<=end and end<=n:
    if sum(li[start:end])==m:
        cnt+=1
        end+=1
    elif sum(li[start:end+1])<m:
        end+=1
    elif sum(li[start:end+1])>m:
        start+=1
print(cnt)
    