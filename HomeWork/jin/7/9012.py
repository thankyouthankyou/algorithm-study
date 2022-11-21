n = int(input())

def sol(inp):
    st=[]
    for i in inp:
        if not st:
            if i==')':
                return False
            else:
                st.append(i)
        else:
            if st[-1]=='(' and i==')':
                st.pop()
            else:
                st.append(i)
    if st:
        return False
    else:
        return True
        
for _ in range(n):
    inp = input()
    if sol(inp):
        print('YES')
    else:
        print('NO')