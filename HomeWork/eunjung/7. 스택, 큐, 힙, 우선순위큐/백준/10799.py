from collections import deque
L = input()
L = L.replace("()", "R")
dq = deque()
ans = 0

for i in range(len(L)):
  if L[i] == "R":
    ans += len(dq)
  elif L[i] == "(":
    dq.append("(")
  elif L[i] == ")":
    dq.pop()
    ans+=1
print(ans)