from collections import defaultdict
# https://docs.python.org/ko/3/library/collections.html#collections.defaultdict

N=int(input())
cards=list(input().split())
have=defaultdict(int) #기본 value값 0
for i in cards:
    have[i] += 1

M=int(input())
check=list(input().split())
for num in check:
    print(have[num], end = " ")