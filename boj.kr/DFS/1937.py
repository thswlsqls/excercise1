import sys
sys.setrecursionlimit(10**9)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)

dp = [[-1]*N for _ in range(N)]

def dfs(y, x):
    if dp[y][x] == -1:
        dp[y][x] = 0

        cur = graph[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N:
                nxt = graph[ny][nx]
                if nxt > cur:
                    dp[y][x] = max(dp[y][x], dfs(ny, nx))
    return dp[y][x]+1

ans = -1e9
for y in range(N):
    for x in range(N):
        ans = max(ans, dfs(y, x))

print(ans)



