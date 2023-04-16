# 예제문제 (3)
# boj.kr/11286 절댓값 힙
# 우선순위 큐

import sys
import heapq as hq

input = sys.stdin.readline
arr = []

for _ in range(int(input())):
    n = int(input())
    if n:
        hq.heappush(arr, (abs(n), n))
    else:
        print(hq.heappop(arr)[1] if arr else 0)