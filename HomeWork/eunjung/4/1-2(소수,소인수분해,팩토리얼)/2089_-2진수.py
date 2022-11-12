N=int(input())
L=""

if N == 0:
  print(0)

else:
  while N != 1:
    if N%-2 == -1:
      L+="1";
      N=(N//-2) +1
    else:
      L+="0";
      N=N//-2
  L += "1"
  
  print(L[::-1])