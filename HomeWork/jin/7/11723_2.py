import sys
input = sys.stdin.readline

n=int(input())
b=set()

for _ in range(n):
    inp = input().split()
    if len(inp)==1:
        if inp[0]=='all':    
            b=set([str(i) for i in range(1,21)])
        elif inp[0]=='empty':    
            b=set()
    elif len(inp)==2:
        cmd,x = inp[0],inp[1]
        x = int(x)
    if cmd=='add':
        b.add(x)
    elif cmd=='remove' and x in b:
        b.remove(x)
    elif cmd=='check':
        if x in b:
            print(1)
        else: print(0)
    elif cmd=='toggle':
        if x in b:
            b.remove(x)
        else: b.add(x)