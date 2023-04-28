N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2
shark_eat_cnt = 0

from collections import deque

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)

def bfs(y, x):
    chk = [[0] * N for _ in range(N)]
    global shark_size
    dq = deque()
    dq.append((y, x))
    eat_list = []

    while dq:
        (y, x) = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and board[ny][nx]<=shark_size and chk[ny][nx] == 0:
                chk[ny][nx] = chk[y][x] + 1
                dq.append((ny, nx))
                if 0 < board[ny][nx] < shark_size:
                    eat_list.append((ny, nx, chk[ny][nx]))

    eat_list.sort(key=lambda x: (x[2], x[0], x[1]))
    return eat_list


ans = 0
def eat_shark():
    for y in range(N):
        for x in range(N):
            if board[y][x] == 9:
                ny = y
                nx = x
                board[y][x] = 0
    while True:
        global ans
        global shark_eat_cnt
        global shark_size

        eat_list = bfs(ny, nx)

        if len(eat_list) == 0:
            break
        else:
            (ny, nx, distance) = eat_list[0]

            shark_eat_cnt += 1
            if shark_size == shark_eat_cnt:
                shark_size += 1
                shark_eat_cnt = 0

            board[ny][nx] = 0
            ans += distance

    return ans

print(eat_shark())






