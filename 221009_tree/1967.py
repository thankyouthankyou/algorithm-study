import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n-1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

visited = [False] * (n+1)
visited[1] = True
depth = [0] * (n+1)

def dfs(x):
  for i, w in graph[x]:
    if visited[i] == False:
      visited[i] = True
      depth[i] = depth[x] + w
      dfs(i)
dfs(1)

a = depth.index(max(depth))

visited = [False] * (n+1)
visited[a] = True
depth = [0] * (n+1)
dfs(a)
print(max(depth))

