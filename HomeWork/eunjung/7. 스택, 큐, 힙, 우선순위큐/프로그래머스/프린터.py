from collections import deque 

def solution(priorities, location):
    dq1 = deque()
    for i in priorities: #큐만듦
        dq1.append(i)
    priorities.sort(reverse=True) #배열 순서 만듦
    answer = 0 #프린트 횟수
    while len(dq1) != 0:
        if dq1[0] == priorities[0]:
            answer += 1
            if location == 0:
                return answer
            dq1.popleft()
            priorities.pop(0)
            location -= 1
        else:
            dq1.append(dq1[0])
            dq1.popleft()
            if location == 0:
                location = len(dq1)-1
            else:
                location -= 1
