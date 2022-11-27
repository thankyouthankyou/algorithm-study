from itertools import permutations as p

def solution(numbers):
    answer = []
    
    number_list = list(p(numbers, len(numbers)))
    for number in number_list:
        answer.append("".join(map(str,number)))
        
    return max(answer)