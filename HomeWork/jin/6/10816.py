n = int(input())
li = list(map(int,input().split()))
m = int(input())
inp = list(map(int,input().split()))

dic = dict()
for i in li:
    dic[i]=dic.get(i,0)+1

for i in inp:
    if i in dic:
        print(dic[i],end=' ')
    else: print(0,end=' ')