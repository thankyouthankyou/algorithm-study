import heapq
import sys

input=sys.stdin.readline

H = []
n = int(input())
for _ in range(n):
    inp = int(input())
    if inp==0:
        if H:
            print(-heapq.heappop(H))
        else: print(0)
    else:
        heapq.heappush(H,-inp)