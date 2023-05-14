N = int(input())

import heapq as hq

nums1 = [] # 양수 최대힙
nums2 = [] # 음수 최소힙
cnt_0 = 0
tot = 0

for _ in range(N):
    num = int(input())
    if num == 0:
        cnt_0 += 1
    if num == 1:
        tot += 1
    if num > 1:
        hq.heappush(nums1, -num)
    if num < 0:
        hq.heappush(nums2, num)

while len(nums1) > 1:
    num1 = -hq.heappop(nums1)
    num2 = -hq.heappop(nums1)
    tot += (num1*num2)
if nums1:
    tot += -hq.heappop(nums1)

while len(nums2) > 1:
    num1 = hq.heappop(nums2)
    num2 = hq.heappop(nums2)
    tot += (num1 * num2)
if nums2:
    if cnt_0 > 0:
        cnt_0 -= 1
        tot += 0
    else:
        tot += hq.heappop(nums2)

print(tot)