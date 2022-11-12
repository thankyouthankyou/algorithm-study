#시간초과
from collections import defaultdict

N=int(input())
dict = defaultdict(int)
for i in range(N):
    num = int(input())
    dict[num] += 1

ans=[k for k,v in dict.items() if max(dict.values()) == v]
print(min(ans))