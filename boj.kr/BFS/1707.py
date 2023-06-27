import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    dq = deque()
    dq.append(node)
    while dq:
        cur = dq.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = 1 if visited[cur] == 2 else 2
                dq.append(nxt)
            elif visited[nxt] == visited[cur]:
                return False
    return True

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    visited = [-1 for _ in range(V+1)]
    flag = True
    for node in range(1, V+1):
        if visited[node] == -1:
            if not bfs(node):
                flag = False

    print("YES" if flag else "NO")