from collections import deque

dx = (1, 1, -1, -1, 2, 2, -2, -2)
dy = (2, -2, 2, -2, 1, -1, 1, -1)

def bfs(x1, y1, x2, y2, I):
    if (x1, y1) == (x2, y2):
        return 0
    dq = deque()
    dq.append((x1, y1))
    board = [[0]*I for _ in range(I)]
    board[x1][y1] = 1

    while dq:
        (x, y) = dq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and not board[nx][ny]:
                if nx == x2 and ny == y2:
                    return board[x][y]
                else:
                    board[nx][ny] = board[x][y] + 1
                    dq.append((nx, ny))

N = int(input())

for _ in range(N):
    I = int(input())
    (x1, y1) = map(int, input().split())
    (x2, y2) = map(int, input().split())

    print(bfs(x1, y1, x2, y2, I))

