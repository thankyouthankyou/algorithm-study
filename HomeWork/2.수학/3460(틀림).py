#이진수

T = int(input())
n = int(input())

num = str(format(n,'b'))
reversed_num = "".join(reversed(num))
print(num)
for i in range(len(reversed_num)):
    if reversed_num[i] == "1":
        print(i, end=" ")