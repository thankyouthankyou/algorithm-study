n = int(input())
# pib=[0,1,1,2,3,5,8,13,21,34,55]
pib = [0, 1]+[0]*(n-1)

for i in range(2, n+1):
    pib[i] = pib[i-1]+pib[i-2]
# print(pib)
print(pib[n])
