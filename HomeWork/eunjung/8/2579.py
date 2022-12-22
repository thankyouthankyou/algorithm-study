N = int(input())
stairs=[0]
for i in range(N):
    stairs.append(int(input()))
if N == 1:
    print(stairs[1])
elif N == 2:
    print(sum(stairs[1:3]))
else:
    dp=[0]
    dp.append(stairs[1])
    dp.append(stairs[1]+stairs[2])
    dp.append(max(stairs[1]+stairs[3], stairs[2]+stairs[3]))
    for i in range(4, N+1):
        dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]))
    print(dp[N])