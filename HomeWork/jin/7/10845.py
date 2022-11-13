from collections import deque
import sys

input = sys.stdin.readline

n=int(input())
b=deque()
for _ in range(n):
    inp = input().split()
    if inp[0]=='push':
        b.append(inp[1])
    if inp[0]=='pop':
        if b:
            print(b.popleft())11
        else:
            print(-1)
    if inp[0]=='size':
        print(len(b))
    if inp[0]=='empty':
        if b:
            print(0)
        else:
            print(1)
    if inp[0]=='front':
        if b:
            print(b[0])
        else:
            print(-1) 
    if inp[0]=='back':
        if b:
            print(b[-1])
        else:
            print(-1) 