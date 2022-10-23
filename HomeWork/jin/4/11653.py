n=int(input())
prime=[]
is_prime=[0,0]+[1]*(n-1)
for i in range(2,n+1):
    if is_prime[i]:
        prime.append(i)
        j=2
        while i*j<=n:
            is_prime[i*j]=0
            j+=1
            
while n!=1:
    for i in prime:
        if n%i==0:
            n//=i
            print(i)
            break