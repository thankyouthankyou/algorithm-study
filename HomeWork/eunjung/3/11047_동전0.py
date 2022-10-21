N, K = map(int, input().split())
moneyList = []
C = 0

for i in range(N):
    m = int(input())
    moneyList.insert(0, m)

for i in moneyList:
    if i > K:
        continue
    C += (K // i)
    K = (K % i)
    if K == 0:
        break
    
print(C)
    

