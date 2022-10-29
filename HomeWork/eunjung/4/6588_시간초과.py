nums = []

#nums에 테스트케이스 넣기
while True:
    num = int(input())
    if num == 0:
        break
    nums.append(num)

m = max(nums)
L = [True] * (m+1)
prime = [] #소수

#max(nums)까지 소수 구해서 prime 리스트 만들기
for i in range(2, int(m**0.5) + 1):
    if L[i] == True:
        for j in range(i+i, m+1, i):
            L[j] = False

for i in range(2, m+1):
    if L[i] == True:
        prime.append(i)

#더해서
for num in nums:
    for i in prime:
        if (num-i) in prime:
            print('{} = {} + {}'.format(num, i, num-i))
            break
        if i == prime[-1]:
            print("Goldbach's conjecture is wrong.")