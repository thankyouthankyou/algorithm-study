#N번째 큰 수
T = int(input())

for _ in range(T):
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    print(L[2])