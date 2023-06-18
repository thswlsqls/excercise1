N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

import sys
sys.setrecursionlimit(10**9)

dp = [[-1 for _ in range(N)] for _ in range(N)]
def dfs(y, x):
    if dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and graph[ny][nx] > graph[y][x]:
                dp[y][x] = max(dfs(ny, nx), dp[y][x])
    return dp[y][x]+1

ans = -1e9
for y in range(N):
    for x in range(N):
        ans = max(ans, dfs(y, x))

print(ans)