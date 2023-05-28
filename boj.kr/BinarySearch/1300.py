N = int(input())
k = int(input())

lo = 0
hi = k
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    cnt =0
    for i in range(1, N+1):
        cnt += min(mid//i, N)

    if cnt >= k:
        hi = mid-1
        ans = mid
    else:
        lo = mid+1

print(ans)
