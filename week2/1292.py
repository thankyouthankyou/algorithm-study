a, b = map(int, input().split())

li = []
i = 1
while len(li) < b:
    li += [i]*i
    i += 1
print(li)
print(sum(li[a-1:b]))
