def inorder_traverse(T):
    if T:
        inorder_traverse(int(E[T][1]))
        print(E[T][0], end="")
        inorder_traverse(int(E[T][2]))

import sys
sys.stdin = open('input_1231.txt')
T = 10
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    V = int(input())
    E = [[0] * 3 for _ in range(V+1)]
    for n in range(V):
        S = input().split()
        p = int(S[0])
        E[p][0] = S[1]
        E[p][1:len(S)-1] = S[2:len(S)]
    print(E)
    inorder_traverse(1)
    print()

