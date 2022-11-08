st = input()
n = int(input())
cursor = len(st)
for _ in range(n):
    inp = input().split()
    if inp[0]=='L' and cursor>0:
        cursor-=1
    elif inp[0]=='D' and cursor<len(inp)-1:
        cursor+=1
    elif inp[0]=='B' and cursor>0:
        st = st[:cursor-1]+st[cursor:]
        cursor-=1
    elif inp[0]=='P':
        st = st[:cursor]+inp[1]+st[cursor:]
        cursor+=1
print(st)
    