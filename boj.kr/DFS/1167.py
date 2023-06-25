import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    I = list(map(int, input().split()))
    s, e = 1, 3
    while e < len(I):
        graph[I[0]].append(I[s:e])
        s += 2
        e += 2

def dfs(node, d):
    for (ne, nd) in graph[node]:
        if visited[ne] == -1:
            visited[ne] = d + nd
            dfs(ne, d + nd)

visited = [-1] * (N+1)
visited[1] = 0
dfs(1, 0)
start = visited.index(max(visited))

visited = [-1] * (N+1)
visited[start] = 0
dfs(start, 0)
print(max(visited))