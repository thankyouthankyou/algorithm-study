import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    inp = list(input().rstrip())
    st1 = []
    st2 = []
    for i in inp:
        if i=="<":
            if st1:
                st2.append(st1.pop())
        elif i==">":
            if st2:
                st1.append(st2.pop())
        elif i=="-":
            if st1:
                st1.pop()
        else: st1.append(i)
    st1.extend(reversed(st2))
    print(''.join(st1))