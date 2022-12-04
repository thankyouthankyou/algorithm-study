import sys
input=sys.stdin.readline

n=int(input())
dp = [0 for i in range(301)]
# array=[0]+[int(input()) for _ in range(n)]
array=[0 for i in range(301)]

for i in range(n):
    array[i+1]=int(input())

dp[1]=array[1]
dp[2]=array[1]+array[2]

for i in range (3,n+1):
    dp[i]=max(dp[i-3]+array[i-1]+array[i],dp[i-2]+array[i])

print(dp[n])