n, m = map(int, input().split())
nums = list(map(int, input().split())) + list(map(int, input().split()))
nums.sort()

print(*nums)