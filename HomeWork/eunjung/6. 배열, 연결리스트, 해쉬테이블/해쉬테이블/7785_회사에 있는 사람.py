n=int(input())
ans = {}
for i in range(n):
    name, commute = input().split()
    if commute == "enter":
        ans[name] = 1
    else:
        del ans[name]
ans = sorted(ans.items(), reverse = True) #list임. [('Askar', 1), ('Artem', 1)]

for i in ans:
    print(i[0])