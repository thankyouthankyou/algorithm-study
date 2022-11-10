n = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
applen = int(input())
for _ in range(applen):
    x,y = map(int,input().split())
    arr[x][y]=2
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

arr[cur_x][cur_y]=1
while 1:
    cnt+=1
    nxt_x = cur_x+dir_listx[cur_dir]
    nxt_y = cur_y+dir_listy[cur_dir]
    if nxt_x<0 or nxt_x>n or nxt_y<0 or nxt_y>n or arr[nxt_x][nxt_y]==1:
        break
    if arr[nxt_x][nxt_y]==2:
        arr[nxt_x][nxt_y]=1
    else: 
        arr[cur_x][cur_y]=0
        arr[nxt_x][nxt_y]=1
    cur_x=nxt_x
    cur_y=nxt_y
    # cnt+=1
    if cnt in change_dir:
        if change_dir[cnt]=='D':
            cur_dir=(cur_dir+1)%4
        elif change_dir[cnt]=='L':
            cur_dir=(cur_dir-1)%4
print(cnt)
    
            
