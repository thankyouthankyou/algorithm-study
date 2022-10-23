from itertools import permutations

a,b=map(int,input().split())
li=list(map(int,input().split()))
li2=sorted(permutations(li, b))
for i in li2:
    print(*i)