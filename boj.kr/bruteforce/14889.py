N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
nums = []
for n in range(N):
    nums.append(n)

from itertools import combinations
from itertools import permutations
diff_list = []
for combi in combinations(nums, N//2):
    start_tot = 0
    link_tot = 0
    startT = list(combi[:])
    linkT = [x for x in nums if x not in startT]
    for permu in permutations(startT, 2):
        start_tot += board[permu[0]][permu[1]]
    for permu in permutations(linkT, 2):
        link_tot += board[permu[0]][permu[1]]
    diff_list.append(abs(start_tot-link_tot))
print(min(diff_list))