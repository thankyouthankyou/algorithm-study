m,n = map(int,input().split())

is_prime=[0,0]+[1]*(n-1)
for i in range(2,n+1):
    if is_prime[i]:
        j=2
        while i*j<=n:
            is_prime[i*j]=0
            j+=1

for i in range(m,n+1):
    if is_prime[i]:
        print(i)