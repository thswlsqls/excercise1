import sys
sys.setrecursionlimit(10**9)

T = int(input())

def dfs(node):
    global team_members
    cycle.append(node)
    visited[node] = 1
    nxt = choose[node]

    if visited[nxt] == 1:
        if nxt in cycle:
            team_members += cycle[cycle.index(nxt):]
    else:
        dfs(nxt)

for i in range(T):
    N = int(input())
    choose = [0] + list(map(int, input().split()))
    team_members = []
    visited = [0]*(N+1)

    for n in range(1, N+1):
        if visited[n] == 0:
            cycle = []
            dfs(n)

    print(N - len(team_members))