#인덱스 에러
from collections import deque
def bfs(n):
    q = deque()
    q.append(n)
    while q:
        loca = q.popleft()
        for i in (loca*2, loca+1, loca-1):
            if 0 <= i <= 100000 and not visited[i]:
                if i == k:
                    return visited[loca] + 1
                else:
                    visited[i] = visited[loca] + 1
                    q.append(i)

n, k = map(int, input().split())
visited = [0 for _ in range(10001)]
print(bfs(n))

# 왜틀린지 모르겠는
import sys
from collections import deque
def bfs(v):
    q = deque([v]) #큐 구현을 위해 deque 사용
    while q:
        v = q.popleft()
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                if i == k:
                    return visited[v] + 1
                else:
                    visited[i] = visited[v] + 1
                    q.append(i)

n, k = map(int, sys.stdin.readline().split())
visited = [0 for i in range(100001)]
print(bfs(n))


#정답코드
import sys
from collections import deque
def bfs(v):
    q = deque([v]) #큐 구현을 위해 deque 사용
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

n, k = map(int, sys.stdin.readline().split())
visited = [0 for i in range(100001)]
print(bfs(n))