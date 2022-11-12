a,b = map(int,input().split())
li1 = list(map(int,input().split()))
li2 = list(map(int,input().split()))
li = li1+li2
print(*sorted(li))