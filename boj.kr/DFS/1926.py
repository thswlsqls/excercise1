import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

def dfs(y, x):
    global cnt
    cnt+=1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<M and graph[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx)

cnt_list = []
for cy in range(N):
    for cx in range(M):
        if graph[cy][cx] == 1 and not visited[cy][cx]:
            visited[cy][cx] = True
            cnt=0
            dfs(cy, cx)
            cnt_list.append(cnt)

if len(cnt_list) > 0:
    print(len(cnt_list))
    print(max(cnt_list))
else:
    print(len(cnt_list))
    print(0)