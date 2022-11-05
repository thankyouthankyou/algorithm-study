from itertools import permutations

n = int(input())
# li = [i for i in range(1,n+1)]
li = list(map(int,input().split()))

if li == sorted(li):
    print(-1)

for i in range(n-1,0,-1):
    if li[i-1]>li[i]:
        for j in range(n-1,0,-1):
            if li[i-1]>li[j]:
                li[i-1],li[j]=li[j],li[i-1]
                li = li[:i]+sorted(li[i:],reverse=True)
                print(*li)
                exit()
                