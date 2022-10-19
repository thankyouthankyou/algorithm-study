from itertools import combinations_with_replacement
a,b=map(int,input().split())
a2=list(range(1,a+1))
for i in combinations_with_replacement(a2,b):
    print(*i)