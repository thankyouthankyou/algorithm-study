import sys
input = sys.stdin.readline

n=int(input())
b=set()

for _ in range(n):
    inp = input().split()
    if inp[0]=='add':
        b.add(inp[1])
    elif inp[0]=='remove' and inp[1] in b:
        b.remove(inp[1])
    elif inp[0]=='check':
        if inp[1] in b:
            print(1)
        else: print(0)
    elif inp[0]=='toggle':
        if inp[1] in b:
            b.remove(inp[1])
        else: b.add(inp[1])
    elif inp[0]=='all':    
        b=set([str(i) for i in range(1,21)])
    elif inp[0]=='empty':    
        b=set()
    