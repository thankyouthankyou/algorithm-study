N = int(input())

#재귀로 구하기 틀림.
# def findPrime(N):
#     for i in range(2, N):
#         if N % i == 0:
#             print(i)
#             N= int(N/i)
#             if N == i:
#                 return
#             else: 
#                 findPrime(N)
# findPrime(N)

n = 2
while N != 1:
    if N%n == 0:
        print(n)
        N= N//n
    else:
        n += 1
    