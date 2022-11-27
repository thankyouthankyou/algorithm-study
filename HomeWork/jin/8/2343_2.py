n, m = map(int, input().split())
li = list(map(int, input().split()))

start = max(li)
end = res = sum(li)
while start <= end :
    mid = (start+end)//2
    cnt = 1
    sumV = 0
    for i in range(n):
        if sumV+li[i] <= mid:
            sumV += li[i]
        else:
            cnt += 1
            sumV = li[i]
        if cnt > m:
            break
    if cnt > m : # 조건을 만족하는 mid의 최솟값을 찾기 위해
        start = mid+1
    else:
        end = mid-1
        res=min(res,mid)
print(res)