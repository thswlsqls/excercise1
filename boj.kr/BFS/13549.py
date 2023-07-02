N, K = map(int, input().split())
from collections import deque
chk = [-1] * 100_001
chk[N] = 0
def bfs():
    dq = deque()
    dq.append(N)
    while dq:
        cur = dq.popleft()
        if chk[K] != -1:
            return chk[K]
        if 0 <= cur*2 <= 100_000 and chk[cur*2] == -1:
            dq.appendleft(cur*2)
            chk[cur*2] = chk[cur]
        if 0 <= cur-1 <= 100_000 and chk[cur-1] == -1:
            dq.append(cur-1)
            chk[cur-1] = chk[cur] + 1
        if 0 <= cur+1 <= 100_000 and chk[cur+1] == -1:
            dq.append(cur+1)
            chk[cur+1] = chk[cur] + 1
print(bfs())