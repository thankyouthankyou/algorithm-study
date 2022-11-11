from collections import deque
dq1 = deque()
N, K = map(int, input().split())

print("<", end="")
for i in range(1,N+1):
    dq1.append(i)

while len(dq1) > 1:
    for i in range(K-1):
        dq1.append(dq1.popleft())
    print(dq1.popleft(),end=", ")

print(dq1.pop(), end=">")

