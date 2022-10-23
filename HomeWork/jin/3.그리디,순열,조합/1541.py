inp = input()
op=[]
for i in inp:
    if i=='+' or i=='-':
        op.append(i)
inp=inp.replace('-','+')
num = list(map(int,inp.split('+')))

# print(op,num)
rs=num[0]
rs2=0
flag=0
for i in range(len(op)):
    if op[i]=='+' and not rs2:
        rs+=num[i+1]
    else:
        rs2+=num[i+1]
if rs2:
    rs-=rs2
print(rs)