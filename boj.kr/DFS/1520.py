M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]

import sys
sys.setrecursionlimit(10**9)

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)
def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    if y == M-1 and x == N-1:
        return 1
    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<M and 0<=nx<N and graph[y][x] > graph[ny][nx]:
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]

print(dfs(0, 0))