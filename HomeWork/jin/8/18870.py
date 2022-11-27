n = int(input())
li = list(map(int,input().split()))
dic = {}
for i,j in enumerate(sorted(list(set(li)))):
    dic[j]=i
rs = []
for i in li:
    rs.append(dic[i])
print(*rs)