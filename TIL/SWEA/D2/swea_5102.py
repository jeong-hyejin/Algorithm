import sys
sys.stdin = open('input_5102.txt')
T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())
    visited = [0] * (V+1)
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        G[start].append(end)
        G[end].append(start)
    ST, ED = map(int, input().split())

    Q = []
    Q.append(ST)
    visited[ST] = 1
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
    if visited[ED] != 0:
        print('#{} {}'.format(tc, visited[ED]-visited[ST]))
    else:
        print('#{} {}'.format(tc, 0))