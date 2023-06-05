N = int(input())
nums = list(map(int, input().split()))
nums.sort()

lo = 0
hi = len(nums)-1
ans = [nums[lo], nums[hi]]
min_abs_tot = abs(nums[lo] + nums[hi])

while lo < hi:
    tot = nums[lo] + nums[hi]
    abs_tot = abs(tot)
    if abs_tot <= min_abs_tot:
        ans[0] = nums[lo]
        ans[1] = nums[hi]
    min_abs_tot = min(min_abs_tot, abs_tot)

    tot = nums[lo] + nums[hi]
    if tot > 0:
        hi -= 1
    elif tot < 0:
        lo += 1
    else:
        break

ans.sort()
print(*ans)