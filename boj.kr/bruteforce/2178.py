# boj.kr/2178 미로 탐색
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N, M = map(int, input().split())
board = [input() for _ in range(N)]

def is_valid_coord(y, x):
    return 0<=y<N and 0<=x<M

def bfs(start_y, start_x):
    chk = [[False] * M for _ in range(N)]
    chk[start_y][start_x] = True
    dq = deque()
    dq.append((start_y, start_x, 1))

    while dq:
        y, x, d = dq.popleft()

        if y == N-1 and x == M-1:
            return d

        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx] and board[ny][nx] == '1':
                chk[ny][nx] = True
                dq.append((ny, nx, nd))

print(bfs(0, 0))