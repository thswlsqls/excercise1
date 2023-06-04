N = int(input())
dp = [[] for _ in range(N)]

if N == 1:
    print(int(input()))
else:
    dp[0] = list(map(int, input().split()))
    dp[1] = list(map(int, input().split()))
    dp[1][0] += dp[0][0]
    dp[1][1] += dp[0][0]
    if N == 2:
        print(max(dp[1][0], dp[1][1]))
    else:
        for i in range(2, N):
            dp[i] = list(map(int, input().split()))
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] += dp[i-1][j]
                elif j == len(dp[i])-1:
                    dp[i][j] += dp[i-1][len(dp[i-1])-1]
                else:
                    dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

        print(max(dp[N-1]))