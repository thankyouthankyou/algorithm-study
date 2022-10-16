current_passenger = 0
max_passenger = 0

for _ in range(10):
    o, i = map(int, input().split())
    current_passenger += (i - o)
    if current_passenger > max_passenger:
        max_passenger = current_passenger
print(max_passenger)