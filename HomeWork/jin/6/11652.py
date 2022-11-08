n = int(input())
dic = dict()
for _ in range(n):
    inp = int(input())
    dic[inp]=dic.get(inp,0)+1

rs = sorted(dic,key=lambda x:(-dic[x],x))
print(rs[0])