from collections import deque
N, K = map(int, input().split())
chk = [0] * 100001

def bfs(N):
    dq = deque()
    dq.append(N)
    while dq:
        cur = dq.popleft()
        if cur == K:
            return chk[cur]
        for nxt in (cur+1, cur-1, cur*2):
            if 0 <= nxt <= 100000 and not chk[nxt]:
               chk[nxt] = chk[cur] + 1
               dq.append(nxt)

print(bfs(N))