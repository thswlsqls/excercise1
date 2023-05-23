N, C = map(int, input().split())
homes = [int(input()) for _ in range(N)]
homes = sorted(homes)

lo = 1
hi = homes[-1] - homes[0]
result = 0

while lo <= hi:
    mid = (lo + hi) // 2
    cur = homes[0]
    cnt = 1
    for i in range(1, len(homes)):
        if homes[i] >= cur + mid:
            cur = homes[i]
            cnt += 1
    if cnt >= C:
        lo = mid +1
        result = mid
    else:
        hi = mid -1

print(result)