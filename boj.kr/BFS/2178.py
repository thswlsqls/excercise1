N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
from collections import deque
def bfs():
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        (cy, cx, d) = dq.popleft()
        if cy == N - 1 and cx == M - 1:
            return d
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == '1' and visited[ny][nx] == 0:
                visited[ny][nx] += 1
                dq.append((ny, nx, d + 1))

print(bfs())