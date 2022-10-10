li = [int(input()) for _ in range(9)]
li.sort()
# print(li)

sumV = sum(li)-100

flag = 0
for i in range(8):
    if flag:
        break
    for j in range(i+1, 9):
        print(i,j)
        if li[i]+li[j] == sumV:
            li.remove(li[j])
            li.remove(li[i])
            flag = 1
            break
for i in li:
    print(i)
