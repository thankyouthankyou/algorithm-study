from ast import Lambda

M, N = map(int, input().split())

L = [True] * (N+1)
L[1] = False

for i in range(2, int(N**0.5) + 1):
    if L[i] == True:
        for j in range(i+i, N+1, i): #range(시작, 마지막, 간격)
            L[j] = False

for i in range(M, N+1):
    if L[i] == True:
        print(i)