dy = (-2, -2, -1, -1, 1, 1, 2, 2)
dx = (-1, 1, -2, 2, -2, 2, -1, 1)
from collections import deque
def bfs(sx, sy, ex, ey, N):
    dq = deque()
    dq.append((sy, sx, 0))
    while dq:
        (cy, cx, d) = dq.popleft()
        if cy == ey and cx == ex:
            return d
        for i in range(8):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<N and graph[ny][nx] == 0:
                graph[ny][nx] += 1
                dq.append((ny, nx, d+1))

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [[0]*N for _ in range(N)]
    (sx, sy) = map(int, input().split())
    (ex, ey) = map(int, input().split())
    print(bfs(sx, sy, ex, ey, N))