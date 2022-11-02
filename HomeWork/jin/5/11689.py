def euler(n):
    rs=n
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            rs*=(i-1)/i
            while n%i==0:
                n//=i
    if n>1:
        rs*=(n-1)/n
    print(int(rs))
      
n=int(input())
euler(n)