N = int(input())
graph = [input() for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
from collections import deque
def bfs(y, x, rgb):
    dq = deque()
    dq.append((y, x))
    while dq:
        (cy, cx) = dq.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if rgb == 'RG':
                if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0 and (graph[ny][nx] == 'R' or graph[ny][nx] == 'G'):
                        visited[ny][nx] += 1
                        dq.append((ny, nx))
            else:
                if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0 and graph[ny][nx] == rgb:
                        visited[ny][nx] += 1
                        dq.append((ny, nx))

visited = [[0]*N for _ in range(N)]
RGB_cnt = 0
for y1 in range(N):
    for x1 in range(N):
        if visited[y1][x1] == 0:
            bfs(y1, x1, graph[y1][x1])
            RGB_cnt += 1
visited = [[0]*N for _ in range(N)]
RG_cnt = 0
for y2 in range(N):
    for x2 in range(N):
        if visited[y2][x2] == 0:
            if graph[y2][x2] == 'R' or graph[y2][x2] == 'G':
                bfs(y2, x2, 'RG')
                RG_cnt += 1
            else:
                bfs(y2, x2, 'B')
                RG_cnt += 1

print(RGB_cnt, end=' ')
print(RG_cnt)