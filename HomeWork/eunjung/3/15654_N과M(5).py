import itertools
N, M = map(int, input().split())
arr= list(map(int, input().split()))
arr.sort()

ans = list(itertools.permutations(arr, M))

for i in ans:
    print(*i)