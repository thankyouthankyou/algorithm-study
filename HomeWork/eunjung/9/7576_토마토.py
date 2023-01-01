m, n = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

from collections import deque

def bfs():
    s = 0
    q = deque()
    count1=0
    countM1=0
    #전체탐색 1찾기
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                q.append((i, j))
                count1+=1
            elif graph[i][j]==-1:
                countM1+=1
    visited_count = count1+countM1
    #익은 토마토가 없을 때
    if count1 == 0:
        return -1
    #모든 토마토가 익어있을 때
    if count1 + countM1 == m*n:
        return 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    visited_count += 1
                    graph[nx][ny] = graph[x][y] + 1
                    s = max(s, graph[x][y] + 1)
                    q.append((nx, ny))
    #모든 곳에 방문해서 토마토를 익혔을 때
    if visited_count == m*n:
        return s - 1
    #빈칸 때문에 못익힌 토마토가 있을 때
    else:
        return -1

print(bfs())

# 92%에서 틀림
# case
# 2 2
# 0 0
# 0 0