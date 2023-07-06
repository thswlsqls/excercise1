N = int(input())
board = [input().strip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]

import sys
sys.setrecursionlimit(10**9)
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
def dfs(y, x):
    global d
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<N and board[ny][nx] == '1' and visited[ny][nx] == 0:
            visited[ny][nx] += 1
            dfs(ny, nx)
            d += 1
    return d

cnt = 0
d_list = []
for y in range(N):
    for x in range(N):
        if board[y][x] == '1' and visited[y][x] == 0:
            visited[y][x] += 1
            d = 1
            d_list.append(dfs(y, x))
            cnt += 1
print(cnt)
for d in sorted(d_list):
    print(d)