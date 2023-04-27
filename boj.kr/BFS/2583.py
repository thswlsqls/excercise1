M, N, K = map(int, input().split())
coord = [list(map(int, input().split())) for _ in range(K)]
board = [[0]*N for _ in range(M)]

for i in range(K):
    for yi in range(coord[i][1], coord[i][3]):
        for xi in range(coord[i][0], coord[i][2]):
            board[yi][xi] = 1

from collections import deque

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)

chk = [[0]*N for _ in range(M)]
def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    size = 1
    while dq:
        (y, x) = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<M and 0<=nx<N and board[ny][nx] == 0 and not chk[ny][nx]:
                chk[ny][nx] = chk[ny][nx] + 1
                dq.append((ny, nx))
                size += 1
    return size

cnt = 0
size_list = []
for y in range(M):
    for x in range(N):
        if board[y][x] == 0 and not chk[y][x]:
            chk[y][x] = chk[y][x] + 1
            size_list.append(bfs(y, x))
            cnt += 1

print(cnt)
print(*sorted(size_list))