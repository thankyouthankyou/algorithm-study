from itertools import permutations

n = int(input())
li = [i for i in range(1,n+1)]
inp = list(map(int,input().split()))

for i in permutations(li,n):
    print(i)