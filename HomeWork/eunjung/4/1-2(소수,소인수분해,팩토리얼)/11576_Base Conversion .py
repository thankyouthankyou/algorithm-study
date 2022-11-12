A, B = map(int, input().split())
m = int(input())
L = list(map(int, input().split()))
L=L[::-1]

num = 0
for i in range(len(L)):
  num += A**i * L[i]

ans=[]
while num >= B:
  ans.insert(0, num % B)
  num = num//B
ans.insert(0, num)

print(*ans)