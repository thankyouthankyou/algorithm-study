n=int(input())
rs=''
if not n:
    print(0)
else:
    while n:
        if n%-2:
            rs='1'+rs
            n=n//-2+1
        else:
            rs='0'+rs
            n//=-2
    print(''.join(rs))