N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for y in range(N):
        for x in range(N):
            if adj[y][x] == 1 or (adj[y][k] == 1 and adj[k][x] == 1):
                adj[y][x] = 1

for _ in adj:
    print(*_)