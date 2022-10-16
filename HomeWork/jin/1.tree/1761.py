n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

parent = [0]*(n+1)
depth = [0]*(n+1)
check = [0]*(n+1)

print(tree)

def dfs(node, depth):
    check[node] = 1
    depth[node] = depth
    for child in tree[node]:
        if not check[child]:
            parent[child] = node
            dfs(child, depth+1)


def find_width(a, b):
    for n1, n2 in tree[a]:
        if n1 == b:
            print(n2)
            return n2

# 공통 조상
def lca(a, b):
    width = 0
    # print('depth',depth[a],depth[b])
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
            width += find_width(a, parent[a])
        else:
            b = parent[b]
            width += find_width(b, parent[b])
    while a != b:
        a = parent[a]
        b = parent[b]
        print(a, b)
        print('tree', tree)
        print(tree[a])
        print(tree[b])
        print(find_width(a, parent[a]))
        print(find_width(a, parent[a]))
        width += find_width(a, parent[a])
        width += find_width(b, parent[b])
    return width


dfs(1, 0)
print(parent, 'par')

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lca(a, b))
