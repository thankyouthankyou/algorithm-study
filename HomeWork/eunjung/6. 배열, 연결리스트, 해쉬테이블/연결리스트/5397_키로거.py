from collections import deque

n = int(input())
for i in range(n):
  dq1 = deque()
  dq2 = deque()
  t = input()
  for word in t:
    if word == '<':
      if len(dq1) != 0:
        dq2.append(dq1.pop())
    elif word == '>':
      if len(dq2) != 0:
        dq1.append(dq2.pop())
    elif word == '-':
      if len(dq1) != 0:
        dq1.pop()
    else:
      dq1.append(word)
  while len(dq2) != 0:
    dq1.append(dq2.pop())
  print("".join(dq1))