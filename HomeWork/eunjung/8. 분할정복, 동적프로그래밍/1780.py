import sys
input=sys.stdin.readline

n=int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

m1=0
zero=0
one=0

def cut(n, paper):
    global m1, zero, one
    if not any (1 or -1 in i for i in paper):
        zero += 1
    elif not any (1 or 0 in i for i in paper):
        m1 += 1
    elif not any (0 or -1 in i for i in paper):
        one += 1        
    else:
        left = []
        mid = []
        right = []
        for i in paper:
            left.append(i[:n//3]) 
            mid.append(i[n//3:2*(n//3)])
            right.append(i[2*(n//3):]) 
        cut(n//3, left[:n//3])
        cut(n//3, left[n//3:2*(n//3)])
        cut(n//3, left[2*(n//3):])
        cut(n//3, mid[n//3:])
        cut(n//3, mid[n//3:2*(n//3)])
        cut(n//3, mid[2*(n//3):])
        cut(n//3, right[:n//3])
        cut(n//3, right[n//3:2*(n//3)])
        cut(n//3, right[2*(n//3):])
        return

cut(n, paper)
print(m1)
print(zero)
print(one)