n=int(input())
a=[input() for _ in range(n)]
b=[]
for i in a:
    if i.find('push')>=0:
        b.append(int(i.split()[1]))
    if i=='pop':
        if len(b):
            print(b.pop())
        else:
            print(-1)
    if i=='size':
        print(len(b))
    if i=='empty':
        if len(b):
            print(0)
        else:
            print(1)
    if i=='top':
        if len(b):
            print(b[-1])
        else:
            print(-1) 