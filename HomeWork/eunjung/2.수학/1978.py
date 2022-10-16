N= int(input())
L= list(map(int, input().split()))

c = 0

for n in L:
    if n == 1:
        continue
    if n == 2 or n == 3:
        c += 1
    else:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                break
            if i == int(n/2):
                c += 1
        
print(c)