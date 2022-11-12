from collections import deque

#입력 부분
n = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
applen = int(input())
for _ in range(applen):
    x,y = map(int,input().split())
    arr[x][y]=1
dirn = int(input())
change_dir = dict() 
for _ in range(dirn):
    sec,dir = input().split()
    change_dir[int(sec)]=dir
    
dir_listx = [0,1,0,-1]
dir_listy = [1,0,-1,0]

cur_dir = 0
cur_x,cur_y = 1,1
cnt = 0

snake = deque([[1,1]])
while 1:
    cnt+=1
    nxt_x = cur_x+dir_listx[cur_dir]
    nxt_y = cur_y+dir_listy[cur_dir]
    if nxt_x<1 or nxt_x>n or nxt_y<1 or nxt_y>n or [nxt_x,nxt_y] in snake:#벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
        break
    if arr[nxt_x][nxt_y]==1:
        arr[nxt_x][nxt_y]=0
        snake.appendleft([nxt_x,nxt_y])
    else: 
        snake.pop()
        snake.appendleft([nxt_x,nxt_y])
    cur_x=nxt_x
    cur_y=nxt_y
    # cnt+=1
    if cnt in change_dir:
        if change_dir[cnt]=='D':
            cur_dir=(cur_dir+1)%4
        elif change_dir[cnt]=='L':
            cur_dir=(cur_dir-1)%4
# print(snake)
print(cnt)
    
            
