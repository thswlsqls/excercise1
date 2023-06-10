A = input()
B = input()

dp = [0 for _ in range(len(B))]

for ai in range(len(A)):
    cnt = 0
    for bi in range(len(B)):
        if cnt < dp[bi]:
            cnt = dp[bi]
        elif A[ai] == B[bi]:
            dp[bi] = cnt + 1

print(max(dp))

