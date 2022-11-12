n = int(input())
order = list(map(int, input().split()))
needToMove = [] # 자리바꿀 숫자


if order == [i for i in range(n, 0, -1)]: #마지막 순열이면 거르기
    print(-1)
else:
    for _ in range(n):
        if order[-2] > order[-1]:
            needToMove.append(order[-1])
            del order[-1]
        else:
            needToMove.append(order[-1])
            needToMove.append(order[-2])
            #needToMove리스트에서 orde[i-1]번째 수보다 큰 수 중 가장 작은 수 찾기
            next=min([i for i in needToMove if i > order[-2]])
            del order[-2:]
            needToMove.remove(next)
            needToMove.sort()
            print(*order, next, *needToMove)
            break
        
# # 메모리 초과
# import itertools

# n = int(input())
# L = list(itertools.permutations(range(1, n+1), n))
# per = tuple(map(int, input().split()))
# if per == L[-1]:
#     print(-1)
# else:
#     next = L[L.index(per)+1]
#     print(*next)