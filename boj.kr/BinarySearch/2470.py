N = int(input())
nums = list(map(int, input().split()))
nums.sort()

p1 = 0
p2 = len(nums)-1
ans = [nums[p1], nums[p2]]
tot = nums[p1] + nums[p2]
min_tot = abs(tot)

while p1 < p2:
    if min_tot > abs(nums[p1] + nums[p2]):
        ans[0] = nums[p1]
        ans[1] = nums[p2]
    min_tot = min(min_tot, abs(nums[p1] + nums[p2]))
    tot = nums[p1] + nums[p2]
    if tot < 0:
        p1 += 1
    elif tot > 0:
        p2 -= 1
    else:
        ans[0] = nums[p1]
        ans[1] = nums[p2]
        break

ans.sort()
print(*ans)