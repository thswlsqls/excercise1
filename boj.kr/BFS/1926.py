N, M = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

from collections import deque

def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    chk[y][x] = 1
    tot = 1
    while dq:
        (cy, cx) = dq.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<M and adj[ny][nx] == 1 and chk[ny][nx] == 0:
                dq.append((ny, nx))
                chk[ny][nx] = 1
                tot += 1
    return tot

chk = [[0 for _ in range(M)] for _ in range(N)]
tot_list = []
for y in range(N):
    for x in range(M):
        if chk[y][x] == 0 and adj[y][x] == 1:
            tot_list.append(bfs(y, x))

print(len(tot_list))
print(max(tot_list) if len(tot_list) > 0 else 0)