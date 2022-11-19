import math
def solution(progresses, speeds):
    answer = []
    T=[]#시간 리스트
    for i in range(len(progresses)):
        t=math.ceil((100-progresses[i])/speeds[i])
        T.append(t)
    num= 0
    for i in range(1, len(T)):
        if T[i-1] < T[i]:
            num += 1
            answer.append(num)
            num = 0
        else:
            num += 1
            T[i]=T[i-1]
        if i == len(T)-1:
            answer.append(num+1)
    return answer
