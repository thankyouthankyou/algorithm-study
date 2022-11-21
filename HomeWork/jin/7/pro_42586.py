def solution(progresses, speeds):
    answer = []
    while progresses:
        n = len(speeds)
        re = 0
        for i in range(n):
            progresses[i]+=speeds[i]
        for i in range(n):
            if progresses[i]>=100:
                re+=1
            else: break
        if re:
            answer.append(re)
        for i in range(re):
            progresses.pop(0)
            speeds.pop(0)
            
    return answer