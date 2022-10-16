import math

def check(num):
    val = 1
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            val = 0
            break

    if num == 1:
        val = 0

    return val

M = int(input())
N = int(input())

sum = 0
min = 10001
for i in range(M, N+1):
    if check(i) == 1:
        sum += i
        if i < min:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
"""소수를 찾는 check 함수 이용
check 함수 내부에서,
탐색하는 범위를
math.sqrt(num)+1 까지로 
설정하는 것이
그냥 num 까지로 하는 것보다
연산시간이 짧음
(400ms -> 80ms)
"""