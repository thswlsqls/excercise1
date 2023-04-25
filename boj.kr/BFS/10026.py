# 1. board를 순회하면서 chk한 칸이 아니면 bfs방식으로 모두 탐색, 영역개수+1
# 2. 비색약자인 경우, 색약자인 경우 각각 탐색
# 3. 각각의 경우의 영역 총 개수를 출력

from collections import deque

N = int(input())
board = [list(input()) for _ in range(N)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def bfs(rgb, x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        (x, y) = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if rgb == 'RG':
                if 0 <= nx < N and 0 <= ny < N and (board[nx][ny] == 'R' or board[nx][ny] == 'G') and not chk[nx][ny] :
                    dq.append((nx, ny))
                    chk[nx][ny] = True
            else:
                if 0<=nx<N and 0<=ny<N and board[nx][ny] == rgb and not chk[nx][ny]:
                    dq.append((nx, ny))
                    chk[nx][ny] = True

R_cnt = 0
G_cnt = 0
B_cnt = 0
chk = [[False]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if board[x][y] == 'R' and not chk[x][y]:
            bfs('R', x, y)
            R_cnt+=1
        elif board[x][y] == 'G' and not chk[x][y]:
            bfs('G', x, y)
            G_cnt+=1
        elif board[x][y] == 'B' and not chk[x][y]:
            bfs('B', x, y)
            B_cnt+=1

RG_cnt = 0
chk = [[False]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if (board[x][y] == 'R' or board[x][y] == 'G') and not chk[x][y]:
            bfs('RG', x, y)
            RG_cnt+=1

print(R_cnt+G_cnt+B_cnt)
print(RG_cnt+B_cnt)

