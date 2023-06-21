import sys
sys.setrecursionlimit(10**9)
def dfs(cur):
    global team
    chk[cur] += 1
    cycle.append(cur)
    nxt = choose[cur]
    if chk[nxt] == 1:
        if nxt in cycle:
            team += cycle[cycle.index(nxt):]
    else:
        dfs(nxt)

T = int(input())
for _ in range(T):
    N = int(input())
    choose = [0] + list(map(int, input().split()))
    chk = [0] * (N+1)
    team = []
    for node in range(1, N+1):
        if chk[node] == 0:
            cycle = []
            dfs(node)
    print(N-len(team))