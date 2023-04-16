# 탐욕법
# boj/kr 11047 동전 0
# 예제문제(2)

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0

for coin in coins:
    ans += K // coin
    K %= coin

print(ans)