import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
chk = [[[0]*M for _ in range(N)] for _ in range(H)]

from collections import deque

dz = (0, 0, 0, 0, 1, -1)
dy = (0, 0, 1, -1, 0, 0)
dx = (1, -1, 0, 0, 0, 0)

def bfs():
    dq = deque()
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if board[z][y][x] == 1:
                    dq.append((z, y, x))
                    chk[z][y][x] = 1

    while dq:
        (z, y, x) = dq.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H and board[nz][ny][nx] == 0 and not chk[nz][ny][nx]:
                chk[nz][ny][nx] = chk[z][y][x] + 1
                board[nz][ny][nx] = 1
                dq.append((nz, ny, nx))

    day_cnt = -1e9
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if board[z][y][x] == 0:
                    return 0
                else:
                    day_cnt = chk[z][y][x] if day_cnt < chk[z][y][x] else day_cnt

    return day_cnt

print(bfs()-1)