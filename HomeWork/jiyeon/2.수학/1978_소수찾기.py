import sys
input = sys.stdin.readline

N = int(input())
number_list = list(map(int, input().split()))

# 소수의 개수를 저장하기 위한 변수
count = 0

# 소수 판별 for문
for i in range(N):
    # 1이면 continue (1은 소수가 아니다)
    if number_list[i] == 1:
        continue
    # 1이 아니라면, 판별하려는 수의 제곱근까지의 자연수에 대해 나누어 떨어지는지 확인. 
    for j in range(2,int(number_list[i]**(1/2))+1):  # for j in range(2,number_list[i])로 해도 시간 초과가 발생하지 않는다.
        if number_list[i] % j == 0:
            break
    # 나누어 떨어지는 게 없다면 소수이므로 count에 1을 더해준다.
    else:
        count += 1

print(count)