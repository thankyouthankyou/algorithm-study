import itertools
N, M = map(int, input().split())

ans = list(itertools.product(range(1, N+1), repeat=M))
for i in ans:
    print(*i)