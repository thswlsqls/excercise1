import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for i in range(N-1):
    (s, e, d) = map(int, input().split())
    graph[s].append([e, d])
    graph[e].append([s, d])

def dfs(node, d):
    for (ne, nd) in graph[node]:
        if visited[ne] == -1:
            visited[ne] = d+nd
            dfs(ne, d+nd)

visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (N+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))