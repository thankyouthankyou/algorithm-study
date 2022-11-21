from collections import deque

def solution(bridge_length, weight, truck_weights):
    bri=deque([0],maxlen=bridge_length)
    cnt=0
    cur_weight=0
    while truck_weights:
        if cur_weight-bri[0]+truck_weights[0]<=weight:
            cur_weight=cur_weight-bri[0]+truck_weights[0]
            bri.append(truck_weights.pop(0))
        else:
            cur_weight=cur_weight-bri[0]
            bri.append(0)
        cnt+=1
        # print(cnt,bri,truck_weights)
    return cnt+bridge_length
            
bridge_length=2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))