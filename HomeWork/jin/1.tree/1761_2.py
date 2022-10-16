import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])
# node부터 각 노드별 거리
# print(tree)


def dfs(node, accumulated_weight):
    for next_node, weight in tree[node]:
        if distance[next_node] == -1:
            distance[next_node] = weight+accumulated_weight
            dfs(next_node, distance[next_node])


# 노드 1번부터 제일 먼 노드

n2 = int(input())
for i in range(n2):
    a, b = map(int, input().split())
    distance = [-1]*(n+1)
    distance[a] = 0
    dfs(a, 0)
    print(distance[b])
    # print(a, b, distance[b])