N, M = map(int, input().split())
graph = [[1e9]*(N+1) for _ in range(N+1)]

for _ in range(M):
    (s, e) = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

for _ in range(1, N+1):
    graph[_][_] = 0
    graph[_][0] = 0

for k in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if graph[s][e] > graph[s][k] + graph[k][e]:
                graph[s][e] = graph[s][k] + graph[k][e]

min_sum = 1e9
ans = 0
for i in range(1, N+1):
    if min_sum >= sum(graph[N+1-i]):
        min_sum = sum(graph[N+1-i])
        ans = N+1-i

print(ans)