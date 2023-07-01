N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

from collections import deque

def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    while dq:
        (cy, cx) = dq.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0:
                if L <= abs(graph[cy][cx]-graph[ny][nx]) <= R:
                    unite_set.add((ny, nx))
                    dq.append((ny, nx))
                    visited[ny][nx] += 1

import math
def unite(unite_set):
    tot = 0
    for (y, x) in unite_set:
        tot += graph[y][x]
    for (y, x) in unite_set:
        graph[y][x] = math.trunc(tot/len(unite_set))
    return len(unite_set)-1

cnt = 0
while True:
    unite_cnt = 0
    visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                visited[y][x] += 1
                unite_set = set()
                unite_set.add((y, x))
                bfs(y, x)
                unite_cnt += unite(unite_set)
    if unite_cnt == 0:
        break
    cnt += 1
print(cnt)