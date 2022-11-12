def divFive(n):
  c=0
  while n >= 5:
    c += n // 5
    n = n // 5
  return c

def divTwo(n):
  c=0
  while n >= 2:
    c += n // 2
    n = n // 2
  return c


n,m=map(int,input().split())
k = n-m
F = divFive(n)-divFive(m)-divFive(k)
T = divTwo(n)-divTwo(m)-divTwo(k)
print(min(F, T))