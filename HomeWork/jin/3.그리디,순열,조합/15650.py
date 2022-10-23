from itertools import combinations
a,b=map(int,input().split())
a2=list(range(1,a+1))
for i in combinations(a2,b):
    print(*i)