N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

def bfs(y, x):
    dq = deque()
    dq.append((y, x))

    while dq:
        (y, x) = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and ((graph[ny][nx] == 0 and visited[ny][nx] == 0) or (graph[ny][nx] == 1)):
                visited[ny][nx] += 1
                if graph[ny][nx] == 1 and visited[ny][nx] >= 2:
                    graph[ny][nx] = 0
                if graph[ny][nx] == 0 and visited[ny][nx] == 1:
                    dq.append((ny, nx))

cnt = 0
while True:
    visited = [[0] * M for _ in range(N)]
    bfs(0, 0)
    visited[0][0] = 1
    cnt += 1
    tot = 0
    for _ in graph:
        tot += sum(_)
    if tot == 0:
        break

print(cnt)