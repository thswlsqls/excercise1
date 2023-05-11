import sys
input = sys.stdin.readline

N, K = map(int, input().split())

import heapq
items = []
for _ in range(N):
    heapq.heappush(items, list(map(int, input().split())))

bags = []
for _ in range(K):
    heapq.heappush(bags, int(input()))

tot = 0
temp_items = []
while bags:
    bag = heapq.heappop(bags)
    while items and bag >= items[0][0]:
        heapq.heappush(temp_items, -heapq.heappop(items)[1])
    if temp_items:
        tot += -heapq.heappop(temp_items)
    elif not items:
        break

print(tot)