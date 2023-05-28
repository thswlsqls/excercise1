N, M = map(int, input().split())
lectures = list(map(int, input().split()))

lo = 0
hi = sum(lectures)
ans = hi

while lo <= hi:
    mid = (lo+hi)//2

    if mid < max(lectures):
        lo = mid + 1
        continue

    sub = 0
    sub_cnt = 1
    for i in range(len(lectures)):
        if (sub + lectures[i]) <= mid:
            sub += lectures[i]
        else:
            sub_cnt += 1
            sub = lectures[i]
    if sub_cnt <= M:
        ans = min(ans, mid)
        hi = mid-1
    else:
        lo = mid+1

print(ans)