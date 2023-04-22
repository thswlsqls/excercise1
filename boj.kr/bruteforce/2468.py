# 1 전체 영역에서 최고, 최저 높이 추출
# 2 최저-1 -> 최고 높이 까지 검사하면서 아래 반복
# - board 를 순회하면서 미방문 안전지대의 경우 안전영역개수 cnt 증감하고
# - dfs 함수를 사용해 방문체크
# - 안전영역개수 cnt가 max인지 검사

import sys
sys.setrecursionlimit(10**6)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
min = min(map(min, board))
max = max(map(max, board))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and chk[nx][ny]==0 and board[nx][ny]>h:
            chk[nx][ny]=1
            dfs(nx, ny, h)

result = -1e9

for h in range(min-1, max):
    chk = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]>h and chk[i][j]==0:
                cnt += 1
                chk[i][j]=1
                dfs(i, j, h)

    result = cnt if result < cnt else result

print(result)