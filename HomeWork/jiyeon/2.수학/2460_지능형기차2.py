res = -1
sum = 0

for i in range(10):
    n, m = map(int, input().split())
    sum -= n
    sum += m
    res = max(res, sum)

print(res)

