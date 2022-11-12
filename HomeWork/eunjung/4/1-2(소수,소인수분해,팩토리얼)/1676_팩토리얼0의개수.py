N= int(input())

#팩토리얼 계산
fac=1
for i in range(1, N+1):
  fac = fac*i

#문자열로 바꾸고 뒤집음
reversed_fac = str(fac)[::-1]

#답찾음
ans=0
for i in range(len(reversed_fac)):
    if reversed_fac[i] == '0':
        ans += 1
    else:
        print(ans)
        break

