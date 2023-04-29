N, K = map(int, input().split())

from collections import deque

chk = [-1 for _ in range(100001)]
def bfs(n):
    dq = deque()
    dq.append(n)
    chk[n] = 0
    while dq:
        x = dq.popleft()

        if chk[K] != -1:
            return chk[K]
        if 0 <= x*2 < 100001 and chk[x*2] == -1:
            dq.appendleft(x*2)
            chk[x*2] = chk[x]
            
        if 0 <= x-1 < 100001 and chk[x-1] == -1:
            dq.append(x-1)
            chk[x-1] = chk[x] + 1

        if 0 <= x+1 < 100001 and chk[x+1] == -1:
            dq.append(x+1)
            chk[x+1] = chk[x] + 1

print(bfs(N))


