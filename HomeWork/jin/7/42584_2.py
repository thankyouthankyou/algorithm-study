def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n-1):
        for j in range(i+1,n):
            if prices[i]>prices[j]:
                answer.append(j-i)
                break
            elif j==n-1:
                answer.append(n-i-1)
    return answer+[0]

prices=[1,2,3,2,3]
print(solution(prices))