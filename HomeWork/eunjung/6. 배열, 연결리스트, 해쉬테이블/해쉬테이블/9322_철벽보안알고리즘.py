N = int(input())
for i in range(N):
    n = int(input())
    key1=list(input().split())
    key2=list(input().split())
    value = [i for i in range(n)]
    key1 = dict(zip(key1, value))
    sentc = list(input().split())
    ans = [0 for i in range(n)]
    for i in range(n):
        ans[key1[key2[i]]] = sentc[i]
    print(*ans)





    # key1=enumerate(key1) #(index, 문자열) => (value: key)