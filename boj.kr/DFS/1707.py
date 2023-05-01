import sys
sys.setrecursionlimit(10**6)
N = int(input())

input = sys.stdin.readline
def dfs(node):
    global flag
    for neighbor in graph[node]:
        if (visited[neighbor] == -1):
            visited[neighbor] = 1 if (visited[node] == 2) else 2
            dfs(neighbor)
        else:
            if visited[node] == visited[neighbor]:
                flag = False
                return


for _ in range(N):
    flag = True
    V, E = map(int, input().split())
    visited = [-1] *(V+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(1, V+1):
        if (visited[i] == -1):
            visited[i] = 1
            dfs(i)
            if (flag == False):
                break

    print("YES" if flag else "NO")

