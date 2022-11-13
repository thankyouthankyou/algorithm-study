def solution(s):
    st = []
    for i in s:
        if not st:
            if i=='(': 
                st.append(i)
            else: return False
        elif st[-1]=='(':
            if i == ')':
                st.pop()
            else:
                st.append(i)
        else:
            st.append(i)
    if st:
        return False
    else:
        return True