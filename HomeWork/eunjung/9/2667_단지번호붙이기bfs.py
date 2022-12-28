n = int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

from collections import deque

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
answer = []

def bfs(x, y):
    q=deque()
    q.append((x, y))
    graph[x][y] = 0
    c= 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    c += 1
    answer.append(c)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)

answer.sort()
print(len(answer))
for i in answer:
    print(i)