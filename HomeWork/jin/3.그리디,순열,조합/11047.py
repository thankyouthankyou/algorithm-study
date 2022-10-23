a,b=map(int,input().split())
array=[int(input()) for _ in range(a)]
array.sort(reverse=True)

cnt=0
for i in array:
    cnt+=b//i
    b=b%i
print(cnt)