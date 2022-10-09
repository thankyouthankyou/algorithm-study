n = int(input())
for _ in range(n):
    number10 = int(input())
    number2 = bin(number10)[2:]
    print(number2)
    li = []
    for i in range(len(number2)-2, -1, -1):
        if number2[i] == 1:
            li.append(i)
print(li)
