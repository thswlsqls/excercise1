N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

def year_after(graph):
    temp = [g[:] for g in graph]
    for gy in range(1, N-1):
        for gx in range(1, M-1):
            if graph[gy][gx] > 0:
                for i in range(4):
                    ny = gy + dy[i]
                    nx = gx + dx[i]
                    if 0<=ny<N and 0<=nx<M and graph[ny][nx] == 0:
                        temp[gy][gx] = temp[gy][gx]-1 if temp[gy][gx]-1>0 else 0
                if temp[gy][gx] > 0:
                    ice_set.add((gy, gx))
    return temp

import sys
sys.setrecursionlimit(10**6)

def dfs(y, x):
    for j in range(4):
        ny = y + dy[j]
        nx = x + dx[j]
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and graph[ny][nx] > 0:
            visited[ny][nx] = True
            dfs(ny, nx)

year_cnt = 0
while True:
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    ice_set = set()
    graph = [g[:] for g in year_after(graph)]
    year_cnt += 1
    for (cy, cx) in ice_set:
        if not visited[cy][cx] and graph[cy][cx] > 0:
            dfs(cy, cx)
            cnt += 1
    if cnt >= 2:
        break
    if len(ice_set) == 0:
        year_cnt = 0
        break
print(year_cnt)