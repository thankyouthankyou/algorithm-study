from collections import deque

def solution(bridge_length, weight, truck_weights):
    bri=deque([0,0],maxlen=bridge_length)
    truck_weights.reverse()
    time=0
    sumv=0
    while truck_weights:
        time+=1
        sumv-=bri[0]
        bri.append(truck_weights.pop())
        sumv+=bri[-1]
        if sumv<=weight:
            pass
        else:
            sumv-=bri[-1]
            truck_weights.append(bri.pop())
            bri.append(0)
    return time+bridge_length