# 1. 집의 좌표들과 치킨집 좌표들을 각각 리스트에 저장
# 2. combinations를 사용해 치킨집 좌표 리스트에서 추출한 M개의 치킨집 좌표들을 순회하면서 아래(3,4,5)를 반복
# 3. 집의 좌표 목록을 순회
# 4. 집에서 치킨집까지 거리를 계산하고 최소 치킨거리를 저장
# 5. 모든 집들의 최소 치킨거리를 더한 값을 최소 치킨거리 리스트에 저장
# 6. 최소 치킨거리 리스트에서 최소값을 출력

from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            homes.append([i,j])
        elif board[i][j] == 2:
            chickens.append([i,j])

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

chicken_d_sum_list = []
for M_chickens in combinations(chickens, M):
    chicken_d_sum = 0
    for a in homes:
        chicken_d = 1e9
        for b in M_chickens:
            chicken_d = distance(a, b) if chicken_d > distance(a, b) else chicken_d
        chicken_d_sum += chicken_d
    chicken_d_sum_list.append(chicken_d_sum)

print(sorted(chicken_d_sum_list)[0])