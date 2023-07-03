R, C = map(int, input().split())
graph = [input() for _ in range(R)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

letters = set(graph[0][0])
max_d = -1e9
def dfs(y, x, d):
    global max_d
    max_d = max(max_d, d)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<R and 0<=nx<C and graph[ny][nx] not in letters:
            letters.add(graph[ny][nx])
            dfs(ny, nx, d+1)
            letters.remove(graph[ny][nx])

dfs(0, 0, 1)
print(max_d)