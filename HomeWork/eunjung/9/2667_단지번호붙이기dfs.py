n = int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
answer = []
c= 1

def dfs(x, y):
    global c
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                c += 1
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            answer.append(c)
            c=1

answer.sort()
print(len(answer))
for i in answer:
    print(i)