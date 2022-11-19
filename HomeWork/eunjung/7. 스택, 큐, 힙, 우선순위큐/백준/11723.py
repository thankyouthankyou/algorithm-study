import sys
input = sys.stdin.readline
N = int(input())
S = 0

for i in range(N):
  C = list(input().split())
  if C[0] == "add":
    S |= (1<<int(C[1])-1)
  elif C[0] == "remove":
    S &= ~(1<<int(C[1])-1)
  elif C[0] == "check":
    if S & (1<<int(C[1])-1) != 0:
      print(1)
    else:
      print(0)
  elif C[0] == "toggle":
    if S & (1<<int(C[1])-1) != 0:
      S &= ~(1<<int(C[1])-1)
    else:
      S |= (1<<int(C[1])-1)
  elif C[0] == "all":
    S = (1<<20)-1
  elif C[0] == "empty":
    S = 0