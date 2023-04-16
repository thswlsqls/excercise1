# boj.kr/11724 연결 요소의 개수

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[0]*N for _ in range(N)]
chk = [False]*N
ans = 0

for _ in range(M):
    u, v = map(lambda x: x-1, map(int, input().split()))
    adj[u][v] = adj[v][u] = 1

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)