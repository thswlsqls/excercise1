N = int(input())
nums = [0] + list(map(int, input().split()))
adj = [0] + []
for _ in range(N):
    adj.append(list(map(int, input().split()))[1:])

from collections import deque
def bfs(nodes):
    dq = deque()
    dq.append(nodes[0])
    nodes.remove(nodes[0])
    while dq:
        cur = dq.popleft()
        for nxt in adj[cur]:
            if nxt in nodes:
                dq.append(nxt)
                nodes.remove(nxt)
    return len(nodes) == 0

import sys
sys.setrecursionlimit(10**6)

def dfs(nodes, node):
    cur = node
    nodes.remove(cur)
    for nxt in adj[cur]:
        if nxt in nodes:
            dfs(nodes, nxt)
    return len(nodes) == 0

from itertools import combinations

diff = []
nodes = [x for x in range(1, N+1)]
for i in range(1, N):
    for combi in combinations(nodes, i):
        tot = 0
        if dfs(list(combi), combi[0]): #bfs(list(combi)):
            rest = [x for x in nodes if x not in list(combi)]
            if dfs(rest, rest[0]): #bfs(rest):
                for c in list(combi):
                    tot += nums[c]
                diff.append(abs(tot - (sum(nums)-tot)))

if len(diff) == 0:
    print(-1)
else:
    print(min(diff))