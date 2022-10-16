import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])
print(tree)

# node부터 각 노드별 거리


def dfs(node, accumulated_weight):
    for next_node, weight in tree[node]:
        if distance[next_node] == -1:
            distance[next_node] = weight+accumulated_weight
            dfs(next_node, distance[next_node])


distance = [-1]*(n+1)
distance[1] = 0
# 노드 1번부터 제일 먼 노드
dfs(1, 0)
# print(distance)

start = distance.index(max(distance))
distance = [-1]*(n+1)
distance[start] = 0
# 지름의 끝에서 제일 먼 노드
dfs(start, 0)

# print(distance)
print(max(distance))
