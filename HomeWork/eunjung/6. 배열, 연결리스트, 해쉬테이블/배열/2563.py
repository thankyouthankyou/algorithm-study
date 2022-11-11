arr = [[0 for i in range(100)] for i in range(100)]

n=int(input())
for i in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+11):
        arr[x][y:y+11] = 1

# for i in range(100):
