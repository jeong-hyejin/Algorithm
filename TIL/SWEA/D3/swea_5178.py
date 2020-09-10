import sys
sys.stdin = open('input_5178.txt')
T = int(input())
for tc in range(1, T+1):

    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    n = N
    while n > 1:
        tree[n//2] += tree[n]
        n -= 1
    print('#{} {}'.format(tc, tree[L]))
