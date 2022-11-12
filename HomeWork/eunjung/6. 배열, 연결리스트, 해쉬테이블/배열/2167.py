# 시간 초과
n, m = map(int, input().split())
arr = []
for i in range(n):
    L = list(map(int, input().split()))
    L_sum=[]
    for i in range(m):
        L_sum.append(L[i])
        L_suma.append(L[i]-)
    arr.append(list(map(int, input().split())))

k=int(input())
for i in range(k):
    i, j, x, y = map(int, input().split())
    for i in range(i-1, x):
        ans += sum(arr[i][j-1:y])
    print(ans)

# 값을 하나하나 더하는 방법으로는 시간 초과가 생길 수 있습니다.

# 어떤 배열의 a의 a[i]에서 a[j]까지의 합은 a[0]에서 a[j]의 합에서 a[0]에서 a[i-1]까지의 합을 뺀 값과 같습니다.

# 이를 이용하여 값을 입력받음과 동시에 요소들의 합을 구해놓고, 어떤 요청에 대해서 단순히 두 요소의 차를 구하는 것만으로 답을 구할 수 있습니다.