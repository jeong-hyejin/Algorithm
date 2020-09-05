'''
DFS를 구현하는데
재귀를 사용하지않고 반복을 통한 방법
출발 정점을 스택에 push하고 방문여부를 설정한다.
스택에 값이 있다면 while반복을 통해 스택의 마지막 값을 pop하고
pop한 값을 인접리스트의 인덱스로 접근하여 인접한 요소가 있는지 찾는다.
인접 요소들을 하나씩 순회하며 방문여부를 확인하고 방문하지 않았던 요소라면,
스택에 push해준다. push를 했다면 다시 while 처음으로 돌아가 반복한다.
'''
def dfs(v):
    stack = []
    stack.append(v)
    visited[v] = 1
    while stack:
        v = stack.pop(-1)
        lst.append(v)
        # print(v, end=" ")
        # if not visited[v]:
        #     visited[w] = 1
        for w in G[v]:
            if not visited[w]:
                visited[w] = 1
                stack.append(w)
                # dfs(w)
    return lst

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    # 정점과 간선의 수를 입력받는다.
    V, E =  map(int, input().split())
    # 간선의 정보를 2차원 배열로 만들고
    e = [list(map(int, input().split())) for _ in range(E)]
    # 2차원 배열의 요소를 모두 담을 리스트를 만든다.
    temp = []
    # e를 전체 순회하면서 temp리스트에 담아준다.
    for i in range(E):
        for j in range(len(e[i])):
            temp.append(e[i][j])
    # ex) temp = [1, 4, 1, 3, 2, 3, 2, 5, 4, 6]
    # 인접리스트를 초기화시킨다.
    # ex) G[[], [], [], [], [], [], []]
    # 범위가 V+1인 이유는 인접리스트에 V를 인덱스로 접근하기 위해서이다! (V는 1부터 시작하는데 인덱스는 0부터 시작하니까)
    G = [[] for _ in range(V+1)]
    for i in range(E):
        # temp의 짝수번째 값은 G의 인덱스로 들어가고 -> (start)
        # temp의 홀수번재 값은 G[짝수]의 값이 된다. -> (end)
        # ex) G=[[], [4, 3], [3, 5], [6], [], []]
        G[temp[2*i]].append(temp[2*i+1])
    # 경로의 존재를 확인할 출발 노드와 도착 노드를 입력받는다.
    S, g = map(int, input().split())
    # 방문 여부를 확인할 리스트를 만들어주고(이 역시 V값을 인덱스로 접근하기위해 V+1개 만든다.)
    visited = [0] * (V+1)
    lst = []

    # 입력받은 출발 노드에서 방문한 값들을 lst에 담았고 그 안에 입력받은 도착 노드가 있다면 경로가 있는 것이르모 1을 출력한다.
    if g in dfs(S):
        print(1)
    else:
        print(0)
    print(lst)