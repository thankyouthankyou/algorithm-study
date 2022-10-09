import sys 

N = int(input())

tree={}
for n in range(N):
  self, left, right = sys.stdin.readline().strip().split()
  tree[self] = [left, right]
# print(tree)
#tree = {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}

def preorder(self):
  print(self, end="")
  if tree[self][0] != '.':
    preorder(tree[self][0])
  if tree[self][1] != '.':
    preorder(tree[self][1])

def inorder(self):
  if tree[self][0] != '.':
    inorder(tree[self][0])
  print(self, end="")
  if tree[self][1] != '.':
    inorder(tree[self][1])

def postorder(self):
  if tree[self][0] != '.':
    postorder(tree[self][0])
  if tree[self][1] != '.':
    postorder(tree[self][1])
  print(self, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')