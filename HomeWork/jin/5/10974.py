from itertools import permutations

n = int(input())
li = [i for i in range(1,n+1)]
inp = list(map(int,input().split()))
# print(li)

flag=0
for i in permutations(li,n):    
    if flag:
        print(*i)
        break
    if list(i)==inp:
        flag =1