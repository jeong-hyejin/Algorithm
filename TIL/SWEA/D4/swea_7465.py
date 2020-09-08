
import sys
sys.stdin = open('input_7465.txt')
'''
2
6 4
1 2
2 5
5 1
4 6
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * (N + 1)
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end = map(int, input().split())
        G[start].append(end)
        G[end].append(start)
    # print(G)
    stack = []
    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            # 연결안되어있는 노드도 cnt에 올려주어야 한다 ㅜㅜ
            # 간선이 방향성을 가지지않기때문에 인접리스트에 비어있는 노드가 있더라도(연결 안되고 혼자 있는 노드)
            # 혼자여도 무리는 무리니까 cnt 추가해줘라
            if len(G[i]) == 0:
                cnt += 1
                continue
            stack.append(G[i][0])
            while stack:
                v = stack.pop()
                # print(v, end=" ")
                visited[v] = True
                for w in G[v]:
                    if not visited[w]:
                        visited[w] = 1
                        stack.append(w)
            # print()
            cnt += 1
    print('#{} {}'.format(tc, cnt))