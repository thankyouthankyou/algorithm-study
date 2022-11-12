from collections import defaultdict

n, m = map(int, input().split())

dict = defaultdict(int)
for i in range(n+m):
    name = input()
    dict[name] += 1

ans = [k for k,v in dict.items() if v==2]
ans.sort()

print(len(ans))
for name in ans:
    print(name)