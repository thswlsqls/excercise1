import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

ice_set = set()
def year_after(graph):
    cnt_0 = 0
    temp = [g[:] for g in graph]
    for y in range(1, N-1):
        for x in range(1, M-1):
            if graph[y][x] > 0:
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0<=ny<N and 0<=nx<M:
                        cnt_0 = cnt_0+1 if graph[ny][nx] == 0 else cnt_0
                temp[y][x] = temp[y][x]-cnt_0 if temp[y][x]-cnt_0 > 0 else 0
                if temp[y][x] > 0:
                    ice_set.add((y, x))
                cnt_0 = 0
    return temp

def dfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not graph[ny][nx] == 0 and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx)

year_cnt = 0
while True:
    visited = [[False] * M for _ in range(N)]
    graph = [g[:] for g in year_after(graph)]
    year_cnt += 1
    cnt = 0
    flag = True
    for (y, x) in ice_set:
        if graph[y][x] > 0:
            flag = False
            if not visited[y][x]:
                dfs(y, x)
                cnt += 1
    if cnt >= 2:
        break
    if flag:
        year_cnt = 0
        break

print(year_cnt)