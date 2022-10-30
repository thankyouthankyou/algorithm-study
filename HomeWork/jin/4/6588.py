li = []

while True:
    n=int(input())
    if n==0:
        break
    li.append(n)
    
m=max(li)
is_prime=[0,0]+[1]*(m-1)
for i in range(2,m+1):
    if is_prime[i]:
        j=2
        while i*j<=m:
            is_prime[i*j]=0
            j+=1

for i in li:
    for j in range(3,i-2):
        if is_prime[j] and is_prime[i-j]:
            print(f"{i} = {j} + {i-j}")
            break