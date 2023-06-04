N = int(input())
wines = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]

if N == 1:
    print(wines[0])
else:
    dp[0] = wines[0]
    dp[1] = wines[0]+wines[1]
    if N == 2:
        print(dp[1])
    else:
        for i in range(2, N):
            dp[i] = max(dp[i-1], dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i])
        print(dp[N-1])