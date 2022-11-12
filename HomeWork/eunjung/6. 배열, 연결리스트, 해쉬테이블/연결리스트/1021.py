N, M = map(int, input().split())
L = list(map(int, input().split()))
ans=min(N-L[0],L[0]-1)
for i in range(1, M):
    ma, mi = max(L[i], L[i-1]), max(L[i], L[i-1])
    ans += min(ma-mi, N-ma+mi)
    N -= 1
print(ans)


1 2 3 4 5 6 7 8 9 10 1
3 4 5 6 7 8 9 10 1  6 vs 3
3 4 5 6 7 8 10 1 4
