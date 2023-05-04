import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    (e, s) = map(int, input().split())
    graph[s].append(e)

def bfs(node):
    dq = deque()
    dq.append(node)
    visited = [False] * (N + 1)
    visited[node] = True

    while dq:
        n = dq.popleft()
        for nxt in graph[n]:
            if not visited[nxt]:
                visited[nxt] = True
                dq.append(nxt)

    return visited.count(True)

cnt_list = [0] * (N+1)
for i in range(1, N+1):
    cnt_list[i] = bfs(i)

for i in range(1, len(cnt_list)):
    if cnt_list[i] == max(cnt_list):
        print(i, end=" ")
