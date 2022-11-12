n, m = map(int,input().split())
dic = dict()
for _ in range(n):
    name = input()
    dic[name]=dic.get(name,0)+1
for _ in range(m):
    name = input()
    dic[name]=dic.get(name,0)+1

rs = [i for i in dic if dic[i]==2]
rs.sort()
print(len(rs))
for i in rs:
    print(i)