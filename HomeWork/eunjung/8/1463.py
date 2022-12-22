N = int(input())

L = [0, 0, 1, 1]
for i in range(4, N+1):
    if i % 6 == 0:
        L.append(min(L[i//2]+1, L[i//3]+1, L[i-1]+1))
    elif i % 2 == 0:
        L.append(min(L[i//2]+1, L[i-1]+1))
    elif i % 3 == 0:
        L.append(min(L[i//3]+1, L[i-1]+1))
    else:
        L.append(L[i-1]+1)

print(L[N])


# answer = 0
# while N != 1:
#     if N >= 3:
#         answer += N%3
#         answer += 1
#         N = N // 3
#     else:
#         N -= 1
#         answer += 1
    