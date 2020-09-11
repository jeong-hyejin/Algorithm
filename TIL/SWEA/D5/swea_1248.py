def DFS(node):
    if node:
        lst.append(tree[node][2])
        DFS(tree[node][2])

def DFS1(node):
    if node:
        lst1.append(tree[node][2])
        DFS1(tree[node][2])

def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

import sys
sys.stdin = open('input_1248.txt')
T = int(input())
for tc in range(1, T+1):

    V, E, N1, N2 = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V+1)]
    cnt = 0
    lst = []
    lst1 = []
    for i in range(E):
        parent = temp[i*2]
        child = temp[i*2+1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent
    # print(tree)
    DFS(N1)
    DFS1(N2)
    # print(lst)
    # print(lst1)
    node_list = []
    for i in lst:
        for j in lst1:
            if i == j:
                node_list.append(i)
    # print(node_list)
    # preorder(node_list[0])
    N = node_list[0]
    # print(type(N))
    preorder(N)
    # preorder(3)
    print('#{} {} {}'.format(tc, N, cnt))
