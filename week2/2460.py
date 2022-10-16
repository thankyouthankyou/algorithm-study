cur = 0
maxV = -1
for i in range(10):
    outP, inP = map(int, input().split())
    cur += inP-outP
    maxV = max(maxV, cur)
print(maxV)
