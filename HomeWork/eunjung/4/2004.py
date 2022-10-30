# n,m = map(int, input().split())

# nCm = 1
# for i in range(n, n-m, -1):
#     nCm *= i
# for i in range(2, m+1):
#     nCm /= i

# C = str(int(nCm))[::-1]

# ans=0
# for i in range(len(C)):
#     if C[i] == '0':
#         ans += 1
#     else:
#         print(ans)
#         break

#2의배수 5의배수 최소값

def div(x,y):
    cnt=0
    while y<=x:
        x=x//y
        cnt+=x
    return cnt
n,m=map(int,input().split())
x1=div(n,5)
x2=div(n-m,5)
x3=div(m,5)
print(x1-x2-x3)