def solution(s):
    a = list(s)
    stack = []
    
    for i in a:
        if i == '(':
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    
    return len(stack)==0
        