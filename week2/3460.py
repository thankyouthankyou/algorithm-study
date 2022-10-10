n = int(input())

for i in range(n):
    num = int(input())
    k = 0
    answer = []
    for i in bin(num)[::-1]:
        if i == '1':
            answer.append(k)
        k += 1
    print(*answer)
