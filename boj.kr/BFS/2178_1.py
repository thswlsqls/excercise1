N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
from collections import deque
def bfs():
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        (cr, cc, d) = dq.popleft()
        if cr == N-1 and cc == M-1:
            return d
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<N and 0<=nc<M and board[nr][nc] == '1' and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dq.append((nr, nc, d+1))

print(bfs())