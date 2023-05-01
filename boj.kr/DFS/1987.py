R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

visited = set(graph[0][0])
max_d = 1

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
def dfs(y, x, d):
    global max_d
    max_d = max(max_d, d)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<R and 0<=nx<C:
            if graph[ny][nx] not in visited:
                visited.add(graph[ny][nx])
                dfs(ny, nx, d+1)
                visited.remove(graph[ny][nx])

dfs(0, 0, max_d)
print(max_d)

