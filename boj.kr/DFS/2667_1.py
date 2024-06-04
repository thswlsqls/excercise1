N = int(input())
board = [input().strip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]

import sys
sys.setrecursionlimit(10**9)
dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)

def dfs(r, c):
    global d
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and board[nr][nc] == '1' and visited[nr][nc] == 0:
            visited[nr][nc] += 1
            dfs(nr, nc)
            d += 1
    return d

cnt = 0
d_list = []
for r in range(N):
    for c in range(N):
        if board[r][c] == '1' and visited[r][c] == 0:
            visited[r][c] += 1
            d = 1
            d_list.append(dfs(r, c))
            cnt += 1

print(cnt)
for d in sorted(d_list):
    print(d)
