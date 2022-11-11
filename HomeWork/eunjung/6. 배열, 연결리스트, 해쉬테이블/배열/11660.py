n,m = map(int,input().split())
board = [[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]
print(board)
# 누적 합 배열 구하기
for i in range(1,n+1):
    for j in range(1,n+1):
        board[i][j] = board[i][j]+board[i-1][j]+board[i][j-1]-board[i-1][j-1]

print(board)