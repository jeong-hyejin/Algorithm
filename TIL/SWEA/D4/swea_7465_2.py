def dfs(v):
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            dfs(w)
import sys
sys.stdin = open('input_7465.txt')
# sys.setrecursionlimit(100000)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * (N + 1)
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end = map(int, input().split())
        G[start].append(end)
        G[end].append(start)

    cnt = 0
    for v in range(1, N+1):
        if not visited[v]:
            cnt += 1
            dfs(v)
    print('#{} {}'.format(tc, cnt))