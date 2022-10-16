N, K = map(int, input().split())

divisorList = []

for i in range(1, N+1):
    if N % i == 0:
        divisorList.append(i)
    if len(divisorList) == K:
        print(i)
        break
if len(divisorList) < K:
    print(0)