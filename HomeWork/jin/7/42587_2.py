def solution(priorities, location):
    answer = 0
    pair = list(enumerate(priorities))
    print(pair)
    while [i for i in pair if i[0]==location]:
        print(pair[0],max(pair))
        if pair[0][1]==max(pair)[0]:
            print('a')
            answer+=1
            pair.pop(0)
        else:
            pair.append(pair.pop(0))
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
# return = 1

print(solution(priorities, location))