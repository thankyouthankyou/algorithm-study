N = int(input())
M = list(map(int, input().split()))
A = int(input())

def deleteNode(num, arr):
  arr[num] = -2
  for i in range(len(arr)):
    if arr[i] == num:
      deleteNode(i, arr)
    
deleteNode(A, M)

answer= 0
for i in range(len(M)):
  if M[i] != -2 and i not in M:
    answer += 1
print(answer)