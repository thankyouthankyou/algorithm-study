import itertools 

N, M = map(int, input().split())
ans = list(itertools.permutations(range(1, N+1), M))

for i in ans:
    print(*i)
