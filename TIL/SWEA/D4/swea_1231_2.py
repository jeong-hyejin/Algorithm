'''
[[0, 0, 0], ['W', '2', '3'], ['F', '4', '5'], ['R', '6', '7'], ['O', '8', 0], ['T', 0, 0], ['A', 0, 0], ['E', 0, 0], ['S', 0, 0]]
'''
def inorder(node):
    if node:
        inorder(int(tree[node][1]))
        print(tree[node][0], end="")
        inorder(int(tree[node][2]))
import sys
sys.stdin = open('input_1231.txt')
T = 10
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    V = int(input())
    tree = [ [] for _ in range(V+1)]
    for _ in range(V):
        S = input().split()
        parent = int(S[0])
        tree[parent].extend(S[1:len(S)])
    # print(tree)
    for i in tree:
        if len(i) < 3:
            for j in range(3-len(i)):
                i.append(0)
    # print(tree)
    inorder(1)
    print()