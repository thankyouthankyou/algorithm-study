n, k = map(int, input().split())

holywater_list = []

def get_divisors(n):
    for i in range(1, n+1):
        if n % i == 0:
            holywater_list.append(i)

get_divisors(n)


if k > len(holywater_list):
    print(0)   
else: 
    print(holywater_list[k-1])
 