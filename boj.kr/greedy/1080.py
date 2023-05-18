N, M = map(int, input().split())
adj_from = [list(map(int, list(input()))) for _ in range(N)]
adj_to = [list(map(int, list(input()))) for _ in range(N)]

def change(y, x):
    for yi in range(y, y+3):
        for xi in range(x, x+3):
            adj_from[yi][xi] = 1 - adj_from[yi][xi]

def isEqual():
    for y in range(N):
        for x in range(M):
            if adj_from[y][x] != adj_to[y][x]:
                return False
    return True

cnt = 0
for y in range(N-2):
    for x in range(M-2):
        if adj_from[y][x] != adj_to[y][x]:
            change(y, x)
            cnt += 1

if isEqual():
    print(cnt)
else:
    print('-1')