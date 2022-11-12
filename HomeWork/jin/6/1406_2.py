import sys
input = sys.stdin.readline
st1 = list(input().rstrip())
# st1 = list(input())
st2 = []
n = int(input())
for _ in range(n):
    inp = input().split()
    if inp[0]=='L' and st1:
        st2.append(st1.pop())
    elif inp[0]=='D' and st2:
        st1.append(st2.pop())
    elif inp[0]=='B' and st1:
        st1.pop()
    elif inp[0]=='P':
        st1.append(inp[1])
st1.extend(reversed(st2))
print(''.join(st1))