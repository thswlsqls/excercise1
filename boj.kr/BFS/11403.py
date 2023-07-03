N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for s in range(N):
        for e in range(N):
            if graph[s][k] == 1 and graph[k][e] == 1:
                graph[s][e] = 1

for row in graph:
    print(*row)