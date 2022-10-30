n=int(input())
li = list(map(int,input().split()))

m=max(li)
is_prime=[0,0]+[1]*(m-1)
for i in range(2,m+1):
    if is_prime[i]:
        j=2
        while i*j<=m:
            is_prime[i*j]=0
            j+=1

cnt=0
for i in li:
    if is_prime[i]:
        cnt+=1
        
print(cnt)