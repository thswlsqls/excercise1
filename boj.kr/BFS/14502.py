# 1. 벽을 세울 수 있는 3개 좌표 추출하는 모든 경우에 대해 아래 반복
# 2. BFS함수를 통해 벽을 세운 후 전염결과 구하기
# 3. 전염후 안전지대 총 개수 계산

from itertools import combinations
import copy
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def bfs(temp):
    chk = [[False] * M for _ in range(N)]
    dq = deque()

    for x in range(N):
        for y in range(M):
            if temp[x][y] == 2:
                dq.append((x, y))

    while dq:
        (x, y) = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and temp[nx][ny] == 0 and not chk[nx][ny]:
                chk[nx][ny] = True
                temp[nx][ny] = 2
                dq.append((nx, ny))

candidates = []
for x in range(N):
    for y in range(M):
        if board[x][y] == 0:
            candidates.append([x, y])

max_cnt_0 = -1e9
for combi in combinations(candidates, 3):
    temp = copy.deepcopy(board)
    for [x, y] in combi:
        temp[x][y] = 1
    bfs(temp)
    cnt_0 = 0
    for row in temp:
        cnt_0 += row.count(0)
    max_cnt_0 = cnt_0 if max_cnt_0 < cnt_0 else max_cnt_0

print(max_cnt_0)




