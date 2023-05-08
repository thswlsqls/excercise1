import heapq

N = int(input())
cards = []
for i in range(N):
    heapq.heappush(cards, int(input()))

tot = 0
if N > 1:
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        tot += (a+b)
        heapq.heappush(cards, a+b)

print(tot)