from collections import deque 
import sys

word = input()
dq1 = deque()
for i in word:
    dq1.append(i)
dq2 = deque()
N = int(input())

for i in range(N):
    c = sys.stdin.readline()
    if c[0] == "L" and len(dq1) != 0:
        dq2.append(dq1.pop())
    if c[0] == "D" and len(dq2) != 0:
        dq1.append(dq2.pop())
    if c[0] == "B" and len(dq1) != 0:
        dq1.pop()
    if c[0] == "P":
        dq1.append(c[2])

while len(dq2) != 0:
    dq1.append(dq2.pop())
print("".join(dq1))
