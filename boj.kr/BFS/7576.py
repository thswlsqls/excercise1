M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

from collections import deque
dq = deque()
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            dq.append((y, x))

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
def bfs():
    while dq:
        (cy, cx) = dq.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<M and board[ny][nx] == 0:
                board[ny][nx] = board[cy][cx] + 1
                dq.append((ny, nx))
    max_cnt = -1e9
    for row in board:
        if row.count(0) > 0:
            return -1
        else:
            max_cnt = max(max_cnt, max(row))
    return max_cnt-1

print(bfs())