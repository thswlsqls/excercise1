import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    nums = sorted(nums, key = lambda x: x[0])
    compare = nums[0][1]
    cnt = 1
    for i in range(1, N):
        if nums[i][1] < compare:
            compare = nums[i][1]
            cnt += 1

    print(cnt)