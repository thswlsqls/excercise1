from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

def bfs():
    chk = [[[0]*2 for _ in range(M)] for _ in range(N)]

    dq = deque()
    dq.append((0, 0, 1))
    chk[0][0][1] = 1

    while dq:
        (y, x, break_left) = dq.popleft()

        if x == M - 1 and y == N - 1:
            return chk[y][x][break_left]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == '0' and not chk[ny][nx][break_left]:
                chk[ny][nx][break_left] = chk[y][x][break_left] + 1
                dq.append((ny, nx, break_left))
            if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == '1' and break_left == 1:
                chk[ny][nx][break_left] = 1
                chk[ny][nx][break_left -1] = chk[y][x][break_left] + 1
                dq.append((ny, nx, break_left-1))

    return -1

print(bfs())