import heapq as h


def solution(scoville, k):
    h.heapify(scoville)  # heapq
    answer = 0
    while scoville[0] < k:  # 최소값이 K보다 작음
        if len(scoville) >= 2:
            h.heappush(scoville, h.heappop(scoville) +
                       h.heappop(scoville) * 2)
            answer += 1
        else:
            return -1
    return answer


scoville = [12, 10, 9, 3, 2, 1]
K = 7
print(solution(scoville, K))