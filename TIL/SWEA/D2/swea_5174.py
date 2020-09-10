def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E+2)]
    cnt = 0
    for i in range(E):
        parent, child = temp[i*2], temp[i*2+1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent
    # print(tree)
    preorder(N)
    print('#{} {}'.format(tc, cnt))