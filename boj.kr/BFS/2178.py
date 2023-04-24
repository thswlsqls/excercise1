from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def bfs():
    chk = [[False]*M for _ in range(N)]
    que = deque()
    que.append((0, 0, 1))
    while que:
        (x, y, d) = que.popleft()

        if x == N-1 and y == M-1:
            return d

        nd = d + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == '1' and not chk[nx][ny]:
                chk[nx][ny] = True
                que.append((nx, ny, nd))

print(bfs())