def dfs(v):
    for w in G[v]:
        if not visited[w]:
            dfs(w)
    visited[v] = True
    print(v, end=" ")

import sys
sys.stdin = open('input_1267.txt')
T = 10
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    edges = list(map(int, input().split()))
    G = [[] for _ in range(V+1)]
    for i in range(E):
        u, v = edges[i*2], edges[i*2+1]
        G[v].append(u)

    for i in range(1, V+1):
        if not visited[i]:
            dfs(i)
    print()