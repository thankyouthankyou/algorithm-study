from itertools import product
a,b=map(int,input().split())
a2=list(range(1,a+1))
for i in product(a2,repeat=b):
    print(*i)