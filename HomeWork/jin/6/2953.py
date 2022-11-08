li = []
for i in range(1,6):
    inp = list(map(int,input().split()))
    li.append([i,sum(inp)])
li.sort(key=lambda x:-x[1])
print(*li[0])
