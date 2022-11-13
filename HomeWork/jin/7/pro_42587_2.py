def solution(priorities, location):
    answer = 0
    pair = list(enumerate(priorities))
    while [i for i in pair if i[0]==location]:
        
        if pair[0][1]==max(r[1] for r in pair):
            answer+=1
            pair.pop(0)
        else:
            pair.append(pair.pop(0))
    return answer

priorities = [2,1,3,2]
location = 2