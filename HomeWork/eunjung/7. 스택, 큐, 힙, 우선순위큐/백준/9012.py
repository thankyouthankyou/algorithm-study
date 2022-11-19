from collections import deque

T = int(input())

for i in range(T):
  C = input()
  if len(C) % 2 == 1:
    print("NO")
    continue
  DQ = deque()
  for i in range(len(C)):
    if C[i] == "(":
      DQ.append("(")
    elif len(DQ) == 0:
      print("NO")
      break
    else:
      DQ.pop()
    if i == len(C)-1:
      if len(DQ) == 0:
        print("YES")
      else:
        print("NO")