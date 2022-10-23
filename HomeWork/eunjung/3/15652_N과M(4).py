import itertools
N, M = map(int, input().split())

ans = list(itertools.combinations_with_replacement(range(1, N+1), M))

for i in ans:
    print(*i)