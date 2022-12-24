import sys
input = sys.stdin.readline
white = 0
blue = 0

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

def cut(n, paper):
    global white, blue

    if not any(1 in i for i in paper):
        white += 1
        return
    elif not any(0 in i for i in paper):
        blue += 1
        return
    else:
        left = []
        right = []
        for i in paper:
            left.append(i[:n//2]) 
            right.append(i[n//2:]) 
        cut(n//2, left[:n//2])
        cut(n//2, left[n//2:])
        cut(n//2, right[:n//2])
        cut(n//2, right[n//2:])
        return

cut(n, paper)
print(white)
print(blue)