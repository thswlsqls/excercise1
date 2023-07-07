N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chickens = []
homes = []
for y  in range(N):
    for x in range(N):
        if board[y][x] == 2:
            chickens.append((y, x))
        if board[y][x] == 1:
            homes.append((y, x))
def get_d(y1, x2, y2, x1):
    return abs(y2-y1) + abs(x2-x1)

from itertools import combinations
chicken_d_sum_list = []
for combi in combinations(chickens, M):
    chicken_d_sum = 0
    for (hy, hx) in homes:
        min_chicken_d = 1e9
        for (cy, cx) in combi:
            min_chicken_d = min(min_chicken_d, get_d(hy, hx, cy, cx))
        chicken_d_sum += min_chicken_d
    chicken_d_sum_list.append(chicken_d_sum)
print(min(chicken_d_sum_list))