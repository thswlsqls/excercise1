M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*(M) for _ in range(N)] for _ in range(H)]

dz = (0, 0, 0, 0, -1, 1)
dy = (-1, 1, 0, 0, 0, 0)
dx = (0, 0, -1, 1, 0, 0)
from collections import deque
def bfs():
    dq = deque()
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if graph[z][y][x] == 1:
                    dq.append((z, y, x))
                    visited[z][y][x] += 1
    while dq:
        (cz, cy, cx) = dq.popleft()
        for i in range(6):
            nz = cz + dz[i]
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=nz<H and 0<=ny<N and 0<=nx<M and graph[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
                visited[nz][ny][nx] = visited[cz][cy][cx] + 1
                graph[nz][ny][nx] = 1
                dq.append((nz, ny, nx))
    ans = -1e9
    for z2 in range(H):
        for y2 in range(N):
            for x2 in range(M):
                if graph[z2][y2][x2] == 0:
                    return 0
                else:
                    ans = visited[z2][y2][x2] if visited[z2][y2][x2] > ans else ans
    return ans

print(bfs()-1)