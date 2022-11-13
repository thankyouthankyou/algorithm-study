from collections import deque
def solution(priorities, location):
    priorities=deque(priorities)
    loc=deque([0]*len(priorities))
    loc[location]=1

    cnt=0
    while True:
        maxv=max(priorities)
        pri1=priorities.popleft()
        pri2=loc.popleft()
        if pri1==maxv:
            cnt+=1
            if pri2==1:
                return cnt
        else:
            priorities.append(pri1)
            loc.append(pri2)