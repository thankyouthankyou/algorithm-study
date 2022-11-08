n = int(input())

li = dict()
for _ in range(n):
    name,access  = input().split()
    if access =="enter":
        li[name]=1
    else:
        del li[name]

rs=sorted(li.keys(),reverse=True)
for i in rs:
    print(i)