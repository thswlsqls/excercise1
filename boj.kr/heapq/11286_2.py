# 예제문제 (3)
# boj.kr/11286 절댓값 힙
# 우선순위 큐

import sys
import heapq as hq

input = sys.stdin.readline
min_heap = []
max_heap = []

for _ in range(int(input())):
    n = int(input())
    if n > 0:
        hq.heappush(min_heap, n)
    elif n < 0:
        hq.heappush(max_heap, -n)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)