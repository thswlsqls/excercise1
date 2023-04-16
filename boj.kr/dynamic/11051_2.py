# boj.kr/11051
# 이항계수 2
#타뷸레이션

MOD = 10007

cache = [[0] * 1001 for _ in range(1001)]
N, K = map(int, input().split())

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD

print(cache[N][K])