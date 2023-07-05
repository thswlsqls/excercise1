N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

space = []
infected = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            space.append((y, x))
        if board[y][x] == 2:
            infected.append((y, x))

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)
from collections import deque
def bfs(y, x, temp):
    dq = deque()
    dq.append((y, x))
    while dq:
        (cy, cx) = dq.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<M and (temp[ny][nx] == 0 or temp[ny][nx] == 2) and visited[ny][nx] == 0:
                visited[ny][nx] += 1
                temp[ny][nx] = 2
                dq.append((ny, nx))

import copy
from itertools import combinations
safe_list = []
for combi in combinations(space, 3):
    visited = [[0] * M for _ in range(N)]
    temp = copy.deepcopy(board)
    for (y1, x1) in combi:
        temp[y1][x1] = 1
    for (y2, x2) in infected:
        visited[y2][x2] += 1
        bfs(y2, x2, temp)
    safe = 0
    for row in temp:
        safe += row.count(0)
    safe_list.append(safe)
print(max(safe_list))