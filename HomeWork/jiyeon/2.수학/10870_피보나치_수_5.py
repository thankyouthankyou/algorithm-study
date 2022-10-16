"""
피보나치 함수를 정의해 사용한다.
n이 0일때는 0, n이 1일때는 1이므로 n<=1 일때는 n을 반환한다.
피보나치 수는 앞의 두 피보나치 수의 합이다.
따라서, n번째 피보나치 수는 (n-1)과 (n-2)의 합이 된다.
"""
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)	# 앞 두 수의 합

n = int(input())
print(fibo(n))
