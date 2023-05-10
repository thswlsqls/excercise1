import sys
input = sys.stdin.readline

N, K = map(int, input().split())

items = []
for _ in range(N):
    items.append(list(map(int, input().split())))
items = sorted(items, key = lambda x:x[1], reverse=True)
weights = []

bags = []
for _ in range(K):
    bags.append(int(input()))

tot = 0
for item in items:
    # av_bags = sorted(list(filter(lambda x: x>=item[0], bags)))
    av_bags = [x for x in bags if x>=item[0]]
    if len(av_bags) > 0:
        bags.remove(min(av_bags))
        tot += item[1]

print(tot)