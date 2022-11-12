n = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
applen = int(input())
for _ in range(applen):
    x,y = map(int,input().split())
    arr[x][y]=1
dirn = int(input())
dic_dir = dict() 
for _ in range(dirn):
    sec,dir = map(int,input().split())
    dic_dir[sec]=dir
    
dir_listx = [0,1,0,-1]
dir_listy = [1,0,-1,0]

cur_dir = 0
cur_x,cur_y = 0,0
cnt = 0

while 1:
    if 0<=cur_x<n+1 and 0<=cur_y<n+1:
        if cnt in dic_dir:
            if dic_dir[cnt]=='D':
                cur_dir=(cur_dir+1)%4
            if dic_dir[cnt]=='L':
                cur_dir=(cur_dir-1)%4
        nxt_x=cur_x+dir_listx[cur_dir]
        nxt_y=cur_y+dir_listy[cur_dir]
        cnt+=1
        if arr[cur_x][cur_y]==1:
            arr[cur_x][cur_y]=0
        cur_x=
            
    else: break