N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        if graph[y][x] == 9:
            (sy, sx) = (y, x)

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)
from collections import deque
fishes = []
def set_fishes(py, px):
    dq = deque()
    dq.append((py, px, 0))
    while dq:
        (y, x, d) = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0:
                visited[ny][nx] += 1
                if graph[ny][nx] == 0 or graph[ny][nx] == shark_size:
                    dq.append((ny, nx, d+1))
                elif graph[ny][nx] < shark_size:
                    fishes.append((ny, nx, d+1))
    fishes.sort(key = lambda x: (x[2], x[0], x[1]))

sec = 0
shark_size = 2
eat_cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    visited[sy][sx] += 1
    graph[sy][sx] = 0
    set_fishes(sy, sx)
    if len(fishes) == 0:
        break
    else:
        sec += fishes[0][2]
        sy = fishes[0][0]
        sx = fishes[0][1]
        eat_cnt += 1
        if eat_cnt == shark_size:
            shark_size += 1
            eat_cnt = 0
        fishes = []
print(sec)