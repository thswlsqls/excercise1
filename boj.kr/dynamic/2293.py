N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

dp = [0 for _ in range(K+1)]
dp[0] = 1

for c in coins:
    for i in range(c, K+1):
        if i-c >= 0:
            dp[i] += dp[i-c]

print(dp[K])