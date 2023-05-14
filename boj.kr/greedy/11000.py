import sys
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort()

import heapq as hq
times_q  = []
hq.heappush(times_q, times[0][1])

for i in range(1, len(times)):
    if times[i][0] < times_q[0]:
        hq.heappush(times_q, times[i][1])
    else:
        hq.heappop(times_q)
        hq.heappush(times_q, times[i][1])

print(len(times_q))
