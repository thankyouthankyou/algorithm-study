L = []
for i in range(9):
    L.append(int(input()))
A = sum(L)-100

def DeleteFakeDwarf(L):
    for i in range(8):
        for j in range(1,9):
            if j <= i:
                continue
            if L[i]+L[j] == A:
                one, two = L[i], L[j]
                L.remove(one)
                L.remove(two)
                return 

DeleteFakeDwarf(L)
L.sort()
    
for i in L:
    print(i)
