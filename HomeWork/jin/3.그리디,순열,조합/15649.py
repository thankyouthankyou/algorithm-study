from itertools import permutations

a,b=map(int,input().split())
arr=list(range(1,a+1))
for i in permutations(arr,b):
    print(*i)