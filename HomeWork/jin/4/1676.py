from math import factorial
a=str(factorial(int(input())))
# print(a)

cnt=0
for i in a[::-1]:
    if i=='0':
        cnt+=1
    else:
        break
print(cnt)