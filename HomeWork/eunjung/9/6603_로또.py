# combination 풀이
import itertools

while True:
    L = list(map(int, input().split()))
    k = L[0]
    arr = L[1:]

    if k == 0:
        break

    for i in itertools.combinations(arr, 6):
        print(*i)
    print()


#dfs 풀이

