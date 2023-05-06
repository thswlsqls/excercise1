N = int(input())
populations = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
nodes = [[0] for _ in range(N)]
for i in range(N):
    nodes[i] = i+1

for i in range(1, N+1):
    relations = list(map(int, input().split()))
    graph[i] = relations[1:]

from collections import deque
def bfs(p_combi):
    dq = deque()
    dq.append(p_combi[0])
    p_combi.remove(p_combi[0])
    while dq:
        node = dq.popleft()
        for nxt in graph[node]:
            if nxt in p_combi:
                dq.append(nxt)
                p_combi.remove(nxt)

    if len(p_combi) == 0:
        return True
    else:
        return False

import sys
sys.setrecursionlimit(10**9)

def dfs(p_combi, node):
    if node in p_combi:
        p_combi.remove(node)
    for nxt in graph[node]:
        if nxt in p_combi:
            p_combi.remove(nxt)
            dfs(p_combi, nxt)

    if len(p_combi) == 0:
        return True
    else:
        return False

from itertools import combinations

cnt_list = []
for i in range(1, N):
    for combi in combinations(nodes, i):
        if dfs(list(combi), combi[0]): #bfs(list(combi)):
            others = [x for x in nodes if x not in list(combi)]
            if dfs(others, others[0]): #bfs(others):
                tot_a = 0
                tot_b = 0
                cnt = 0
                for idx in combi:
                    tot_a += populations[idx]
                tot_b = sum(populations) - tot_a
                cnt = abs(tot_a - tot_b)
                cnt_list.append(cnt)

cnt_list.sort()
if len(cnt_list) == 0:
    print(-1)
else:
    print(cnt_list[0])