# 1. 깊이우선탐색 방식으로 단지 수 구하기
# 2. 깊이우선탐색 하면서 단지 내 집 개수 구하기

import sys
sys.setrecursionlimit(10**6)

N = int(input())
board = [list(input()) for _ in range(N)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

chk = [[False]*N for _ in range(N)]
count = 0

def dfs(x, y, cnt):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == '1' and not chk[nx][ny]:
            cnt += 1
            chk[nx][ny] = True
            cnt = dfs(nx, ny, cnt)
    return cnt

cnt_list = []
for x in range(N):
    for y in range(N):
        if board[x][y] == '1' and not chk[x][y]:
            chk[x][y] = True
            count += 1
            cnt_list.append(dfs(x, y, 1))

print(count)
for cnt in sorted(cnt_list):
    print(cnt)