N, K = map(int, input().split())
from collections import deque
def bfs(N):
    visited = [0] * 100001
    visited[N] += 1
    dq = deque()
    dq.append((N, 0))
    while dq:
        (cur, cnt) = dq.popleft()
        if cur == K:
            return cnt
        for nxt in (cur*2, cur+1, cur-1):
            if 0<=nxt<100001 and visited[nxt] == 0:
                visited[nxt] += 1
                dq.append((nxt, cnt+1))
print(bfs(N))