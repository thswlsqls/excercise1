N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

clist = [1 for _ in range(N)]
idx = 0

for stand in nums:
    for compr in nums:
        if stand[0] < compr[0]:
            clist[idx] = clist[idx] + 1 if stand[1] < compr[1] else clist[idx]

    idx += 1

print(*clist)