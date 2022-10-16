import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    li = list(map(int,input().split()))
    for i in range(1,len(li)-2,2):
        tree[li[0]].append([li[i],li[i+1]])
# print(tree)

def dfs(node,accumulated_weight):
    for next_node,weight in tree[node]:
        if distance[next_node]==-1:
            distance[next_node]=weight+accumulated_weight
            dfs(next_node,distance[next_node])

distance = [-1]*(n+1)
distance[1]=0
dfs(1,0)
# print(distance)

start = distance.index(max(distance))
distance = [-1]*(n+1)
distance[start]=0
dfs(start,0)

# print(distance)
print(max(distance))