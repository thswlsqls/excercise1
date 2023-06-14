N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
from collections import deque

def bfs():
    chk = [[0 for _ in range(M)] for _ in range(N)]
    dq = deque()
    dq.append((0, 0))
    chk[0][0] = 1
    while dq:
        (cy, cx) = dq.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<M and ((graph[ny][nx] == 0 and chk[ny][nx] == 0) or (graph[ny][nx] == 1 and not chk[ny][nx] > 2)):
                chk[ny][nx] += 1
                if graph[ny][nx] == 0:
                    dq.append((ny, nx))
                if graph[ny][nx] == 1 and chk[ny][nx] == 2:
                    graph[ny][nx] = 0

def is_no_cheese_left():
    tot = 0
    for _ in graph:
        tot += sum(_)
    return tot == 0

hours = 0
while True:
    if is_no_cheese_left():
        break
    bfs()
    hours += 1

print(hours)