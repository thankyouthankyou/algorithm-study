inp = input()
st = []
cnt, rs = 0, 0
for i in inp:
    if not st or i=='(':
        cnt+=1
    elif st[-1]=='(' and i ==')':
        cnt-=1
        rs+=cnt
    elif st[-1]==')' and i ==')':
        rs+=1
        cnt-=1
    st.append(i)
print(rs)