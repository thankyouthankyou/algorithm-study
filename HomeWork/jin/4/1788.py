n=int(input())

if n<0 and n%2==0:
    print(-1)
elif n>0 or n%2==1:
    print(1)
else: print(0)

fibo=[0,1]
for i in range(abs(n)-1):
    fibo.append(fibo[i]%1000000000+fibo[i+1]%1000000000)
print(fibo[abs(n)]%1000000000)