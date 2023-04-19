from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
tot = 0
answer = 0

for combi in combinations(nums, 3):
 tot = sum(combi)
 if tot <= M:
  answer = tot if tot > answer else answer

print(answer)
