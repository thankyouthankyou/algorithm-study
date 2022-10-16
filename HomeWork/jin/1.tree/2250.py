n = int(input())
tree = [[] for _ in range(n+1)]
row = [[] for _ in range(n+1)]
is_root = [0]*(n+1)
num = 1

# 중위순회


def inorder(root, level):
    global num
    if tree[root][0] != -1:
        inorder(tree[root][0], level + 1)
    row[level].append(num)
    num += 1
    if tree[root][1] != -1:
        inorder(tree[root][1], level + 1)


# 트리 입력 및 루트 노드 확인
for _ in range(n):
    node, left, right = map(int, input().split())
    tree[node].append(left)
    tree[node].append(right)
    is_root[node] += 1
    if left != -1:
        is_root[left] += 1
    if right != -1:
        is_root[right] += 1

root = is_root.index(1)
inorder(root, 1)

# 최대 넓이
# print(row)
level = 1
width = 0
for i in range(len(row)):
    if row[i] and width < max(row[i])-min(row[i])+1:
        width = max(row[i])-min(row[i])+1
        level = i
print(level, width)
