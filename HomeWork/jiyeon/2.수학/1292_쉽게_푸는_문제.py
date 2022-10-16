#1292번 쉽게 푸는 문제

a, b = map(int,input().split())
i=1
nlist = [1]
ncul = [1]
while True:
    i += 1
    nlist.append(i) # [1,2,3,4,5...]
    ncul.append(i + ncul[i-2]) #[1,3,6,...]
    if b <= (i + ncul[i-2]):
        break
answer = 0
for j in range(a,b+1):
    if j == 1:
        answer += 1
    for i in range(len(ncul)):
        if j >ncul[i] and j <= ncul[i+1]:
            answer += nlist[i+1] # a번째 숫자부터 b번째 숫자까지의 합
print(answer)