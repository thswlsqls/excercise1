N = int(input())
cards = [0]+list(map(int, input().split()))
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(1, N+1):
    dp[1][_] = cards[1]*_

for ci in range(2, len(cards)):
    for ni in range(ci, N+1):
        dp[ci][ni] = max(max(dp[ci-1][ni]
                             , dp[ci-1][ni-ci] + cards[ci])
                             , dp[ci][ni-ci]+cards[ci])
        for _ in range(1, ni+1):
            dp[ci][ni] = max(dp[ci][ni], dp[ci][ni-_]+cards[_])
ans = -1e9
for y in range(len(dp)):
    for x in range(len(dp[y])):
        ans = max(ans, dp[y][x])

print(ans)