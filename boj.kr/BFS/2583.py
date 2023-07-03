M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
for _ in range(K):
    (x1, y1, x2, y2) = map(int, input().split())
    for cy in range(y1, y2):
        for cx in range(x1, x2):
            graph[cy][cx] += 1

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)
from collections import deque
visited = [[0]*N for _ in range(M)]
def bfs(y, x):
    cnt = 1
    dq = deque()
    dq.append((y, x))
    while dq:
        (cy, cx) = dq.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<M and 0<=nx<N and graph[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] += 1
                dq.append((ny, nx))
                cnt += 1
    return cnt

cnt_list = []
b_cnt = 0
for fy in range(M):
    for fx in range(N):
        if graph[fy][fx] == 0 and visited[fy][fx] == 0:
            visited[fy][fx] += 1
            cnt_list.append(bfs(fy, fx))
            b_cnt += 1

print(b_cnt)
print(*sorted(cnt_list))