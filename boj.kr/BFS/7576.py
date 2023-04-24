# 1. deque에 익은 토마토 좌표를 모두 저장
# 2. dfs 방식으로 deque를 검사하면서 상화좌우 안익은 토마토는 현재토마토 좌표의 값의 + 1의 값을 갖도록 저장
# 3. 익은 토마토로 변경된 토마토의 좌표를 deque에 저장
# 4. 전제 좌표 값을 순회하면서 0이 있으면 -1을 출력, 0이 없으면 좌표 값 중에서 최대-1을 출력

from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

dq = deque()
for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            dq.append((x, y))
def bfs():
    while dq:
        (x, y) = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1
                    dq.append((nx, ny))
    max_cnt = -1e9
    for x in range(N):
        for y in range(M):
            if board[x][y] == 0:
                return -1
            else:
                max_cnt = board[x][y] if max_cnt < board[x][y] else max_cnt
    return max_cnt-1

print(bfs())