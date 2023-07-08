N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

import sys
sys.setrecursionlimit(10**9)
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
def dfs(y, x, h):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0:
            if board[ny][nx] >= h:
                visited[ny][nx] = 1
                dfs(ny, nx, h)

min_h = 1e9
max_h = -1e9
min_h = min(map(min, board))
max_h = max(map(max, board))
cnt_list = []
for h in range(min_h, max_h+1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for y2 in range(N):
        for x2 in range(N):
            if board[y2][x2] >= h and visited[y2][x2] == 0:
                visited[y2][x2] = 1
                dfs(y2, x2, h)
                cnt += 1
    cnt_list.append(cnt)
print(max(cnt_list))