N, M, V = map(int,input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
print(graph)

for i in range(N+1):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

print(graph)

#DFS구현: 깊이우선탐색 3가지
# visited_dfs = [0]*(N+1)
# def dfs(v):
#     visited_dfs[v] = 1
#     print(v, end=' ')
#     for i in range(N+1):
#         if visited_dfs[i] == 0 and graph[i][v]:
#             dfs(i)
# dfs(1)

#BFS구현: 너비우선탐색
visited_bfs = [0] * (N+1)
from collections import deque
def bfs(v):
    visited_bfs[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in range(N+1):
            if visited_bfs[i] == 0 and graph[i][node]:
                queue.append(i)
                visited_bfs[i] = 1