import sys

N = int(sys.stdin.readline()) #14
s = []

for _ in range(N):
  m = sys.stdin.readline().split()
  order = m[0]
  if order == "push":
    s.append(int(m[-1]))
  elif order == "pop":
    if len(s)==0:
      print(-1)
    else:
      print(s.pop())
  elif order == "size":
    print(len(s))
  elif order == "empty":
    if len(s) == 0:
      print(1)
    else: 
      print(0)
  elif order == "top":
    if len(s) == 0:
      print (-1)
    else:
      print(s[-1])