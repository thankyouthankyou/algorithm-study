nums = []

#nums에 테스트케이스 넣기
while True:
    num = int(input())
    if num == 0:
        break
    nums.append(num)

m = max(nums)
L = [True] * (m+1)

#max(nums)까지 소수 구해서 prime 리스트 만들기
for i in range(2, int(m**0.5) + 1):
    if L[i] == True:
        for j in range(i+i, m+1, i):
            L[j] = False

#더해서
for num in nums:
    for i in range(3, m-2):
        if L[i] and L[num-i]:
            print('{} = {} + {}'.format(num, i, num-i))
            break
        if i == m-3:
            print("Goldbach's conjecture is wrong.")