import sys
n = int(sys.stdin.readline()) # 이게 map보다 더 메모리와 시간상효율적
nums = list(map(int, sys.stdin.readline().split()))
print(min(nums), max(nums))
