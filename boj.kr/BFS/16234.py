N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    unite_country_set = set()

    while dq:
        (y, x) = dq.popleft()
        unite_country_set.add((y, x))
        chk[y][x] += 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and chk[ny][nx] == 0:
                if L <= abs(board[y][x]-board[ny][nx]) <= R:
                    unite_country_set.add((ny, nx))
                    chk[ny][nx] = chk[y][x] + 1
                    dq.append((ny, nx))

    return list(unite_country_set)

day_count = 0
while True:
    chk = [[0 for _ in range(N+1)] for _ in range(N+1)]
    is_move = 0

    for y in range(N):
        for x in range(N):
            if chk[y][x] == 0:
                chk[y][x] += 1
                unite_country_list = bfs(y, x)

                if len(unite_country_list) > 1:
                    is_move = 1
                    avg = sum([board[ny][nx] for (ny, nx) in unite_country_list]) // len(unite_country_list)
                    for (i, j) in unite_country_list:
                        board[i][j] = avg

    if is_move == 0:
        break
    day_count += 1

print(day_count)