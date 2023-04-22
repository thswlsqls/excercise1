from itertools import combinations
from itertools import permutations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
nums = []
for _ in range(N):
    nums.append(_+1)

min = 1e9
startT = []
linkT = []

for combi in combinations(nums, N//2):
    startT = list(combi[:])
    linkT = [x for x in nums if x not in startT]
    startTP = 0
    linkTP = 0
    for permu in permutations(startT, 2):
        startTP += board[permu[0]-1][permu[1]-1]
    for permu2 in permutations(linkT, 2):
        linkTP += board[permu2[0]-1][permu2[1]-1]
    min = abs(startTP - linkTP) if min > abs(startTP - linkTP) else min

print(min)


