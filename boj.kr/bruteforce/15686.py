# 집의 좌표, 치킨집 좌표를 각각 저장
# 집의 좌표 리스트를 순회하면서 combinations를 사용해 치킨집 좌표 리스트에서 추출한 M개의 치킨집 좌표를 대상으로
# 치킨거리를 계산하고 최소값인지 검사

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

from itertools import combinations

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for a in homes:
    tot = 0
    for combi in combinations(chickens, M):
        min = 1e9
        for b in combi:
            min = distance(a, b) if min > distance(a, b) else min
        tot += min

