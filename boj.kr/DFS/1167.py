import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(N):
    nums = list(map(int, input().split()))
    s, e = 1, 3
    while e < len(nums):
        graph[nums[0]].append(nums[s:e])
        s +=2
        e +=2

def dfs(node, d):
    for (ne, nd) in graph[node]:
        if visited[ne] == -1:
            visited[ne] = d + nd
            dfs(ne, d + nd)

visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (N+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))