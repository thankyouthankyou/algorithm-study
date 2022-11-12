n = int(input())
for _ in range(n):
    m = int(input())
    key1 = list(input().split())
    key2 = list(input().split())
    cryp = list(input().split())
    rule = [0]*m
    rs= [0]*m
    for i in range(m):
        rule[key2.index(key1[i])]=i
    for i in range(m):
        rs[rule[i]]=cryp[i]
    print(*rs)