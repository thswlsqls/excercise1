N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

times = sorted(times, key=lambda x : x[0])
times = sorted(times, key=lambda x : x[1])

last_e = 0
cnt = 0
for [s, e] in times:
    if s >= last_e:
        cnt += 1
        last_e = e

print(cnt)