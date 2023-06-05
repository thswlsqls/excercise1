import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
min_w = 1e9
max_w = -1e9

for _ in range(M):
    (y, x, w) = map(int, input().split())
    min_w = min(min_w, w)
    max_w = max(max_w, w)
    adj[y].append((x, w))
    adj[x].append((y, w))

s, e = map(int, input().split())

from collections import deque
def bfs(limit_w):
    dq = deque()
    dq.append(s)
    visited = [False for _ in range(N + 1)]
    visited[s] = True
    while dq:
        cur = dq.popleft()
        for nxt, weight in adj[cur]:
            if not visited[nxt] and limit_w <= weight:
                visited[nxt] = True
                dq.append(nxt)
                if nxt == e:
                    return True
    return False

lo = min_w
hi = max_w
ans = lo

while lo <= hi:
    mid = (lo+hi)//2
    if bfs(mid):
        lo = mid+1
        ans = mid
    else:
        hi = mid-1

print(ans)