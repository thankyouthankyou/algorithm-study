def solution(array, commands):
    answer=[]
    for i,j,k in commands:
        array2=array[i-1:j]
        answer.append(sorted(array2)[k-1])
    return answer