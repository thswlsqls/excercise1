N, M = map(int, input().split())
R = [[] for _ in range(N+1)]

for _ in range(M):
    (e, s) = map(int, input().split())
    R[s].append(e)

from collections import deque

def bfs(start_node):
    dq = deque()
    dq.append(start_node)
    chk[start_node] = 1
    while dq:
        cur = dq.popleft()
        for nxt in R[cur]:
            if chk[nxt] == 0:
                chk[nxt] = 1
                dq.append(nxt)
    return sum(chk)

tot_list = [0] * (N+1)
for sn in range(1, N+1):
    chk = [0] * (N+1)
    tot_list[sn] = bfs(sn)

for i in range(1, N+1):
    if tot_list[i] == max(tot_list):
        print(i, end=" ")