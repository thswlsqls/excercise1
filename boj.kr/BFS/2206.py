N, M = map(int, input().split())
graph = [input() for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)
from collections import deque
def bfs():
    dq = deque()
    dq.append((0, 0, 1, 1))
    visited[0][0][1] += 1
    while dq:
        (cy, cx, left, d) = dq.popleft()
        if cy == N-1 and cx == M-1:
            return d
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<M and visited[ny][nx][left] == 0:
                if graph[ny][nx] == '1' and left == 1:
                    dq.append((ny, nx, 0, d+1))
                    visited[ny][nx][0] += 1
                elif graph[ny][nx] == '0':
                    dq.append((ny, nx, left, d+1))
                    visited[ny][nx][left] += 1
    return -1
print(bfs())