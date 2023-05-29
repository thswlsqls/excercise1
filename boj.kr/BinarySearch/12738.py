N = int(input())
nums = list(map(int, input().split()))

LIS = []
LIS.append(nums[0])

from bisect import bisect_left

for i in range(1, len(nums)):
    if LIS[-1] < nums[i]:
        LIS.append(nums[i])
    else:
        LIS[bisect_left(LIS, nums[i])] = nums[i]

print(len(LIS))