# boj.kr/11051
# 이항계수 2
# 메모이제이션

import sys
sys.setrecursionlimit(10 ** 7)

MOD = 10007
cache = [[0] * 1001 for _ in range(1001)]
N, K = map(int, input().split())

def bino(n, k):
    if cache[n][k]:
        return cache[n][k]

    if k == 0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n-1, k-1) + bino(n-1, k)
        cache[n][k] %= MOD

    return cache[n][k]

print(bino(N, K))