import sys
sys.stdin = open('input_1238.txt')
T = 10
for tc in range(1, T+1):
    # 데이터 길이와 시작점
    N, ST = map(int, input().split())
    # 간선의 정보 입력받기
    temp = list(map(int, input().split()))
    # 방문리스트를 데이터 길이 + 1만큼 만들고 0으로 초기화 (인덱스는 0부터 시작하므로)
    visited = [0] * (N+1)
    # 노드의 번호가 가장 큰 값까지 인덱스로 사용되기때문에 인접리스트를 max(temp)까지 만들고 마찬가지로 +1을 더한다.
    G = [[] for _ in range(max(temp)+1)]
    # 간선이 방향성이 없기때문에 N//2까지만 반복을 돌며 인접리스트에 저장한다.
    for i in range(N//2):
        start, end = temp[i*2], temp[i*2+1]
        G[start].append(end)
    # queue를 만들고
    Q = []
    # 시작노드를 enqueue
    Q.append(ST)
    # enqueue하면서 방문여부를 1로 바꿔준다
    visited[ST] = 1
    # queue가 비어있지않다면
    # queue의 맨 처음 요소를 pop하여 노드로 사용하고 인접 요소들을 확인하여 방문하지 않았다면 enqueue해준다
    # enqueue해주면서 visited[v] + 1 해주며 거리를 저장한다.
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
    # visited에서 가장 큰 값의 인덱스를 출력한다
    maxV = 0
    for idx in range(1, N):
        if visited[maxV] <= visited[idx]:
            maxV = idx
    print('#{} {}'.format(tc, maxV))