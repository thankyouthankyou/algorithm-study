import sys
input = sys.stdin.readline

n, m = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]
m, k = map(int,input().split())
B = [list(map(int,input().split())) for i in range(m)]

answer = []
for i in range(n):
    for j in range(k):
        a = 0
        for k in range(m):
            a += (A[i][k]*B[k][j])
        answer.append(a)
print(*answer)
