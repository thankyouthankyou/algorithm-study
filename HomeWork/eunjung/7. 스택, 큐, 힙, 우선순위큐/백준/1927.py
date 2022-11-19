from heapq import heappush, heappop
import sys

num = int(input())

heap = []
for i in range(num):
  order = int(sys.stdin.readline())
  if order == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heappop(heap))
  else:
    heappush(heap, order)