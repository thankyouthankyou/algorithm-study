def Pisano_period(num):
  answer = 2
  mod1, mod2 = 2, 3
  while True:
    if mod1 % num == 1 and mod2 % num == 1:
      break
    answer += 1
    mod1, mod2 = mod2, (mod1 + mod2) % num
  return answer

#(f(n-2) % m + f(n-1) % m) % m = f(n) % m

n=int(input())
for _ in range(n):
  a, b = map(int,input().split())
  print(a,Pisano_period(b))