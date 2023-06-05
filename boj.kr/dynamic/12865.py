N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N)]

for n in range(N):
    for k in range(K+1):
        w = items[n][0]
        v = items[n][1]
        if k < w:
            if n == 0:
                dp[n][k] = 0
            else:
                dp[n][k] = dp[n-1][k]
        else:
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-w]+v)

print(dp[N-1][K])