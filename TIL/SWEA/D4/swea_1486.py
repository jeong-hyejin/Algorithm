def dfs(k, sumV):
    global minV
    if sumV > minV:
        return
    if k == N:
        if sumV >= B:
            minV = sumV
        return
    else:
        visited[k] = 1
        dfs(k+1, sumV+heights[k])
        visited[k] = 0
        dfs(k+1, sumV)
import sys
sys.stdin = open('input_1486.txt')
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    visited = [0] * N
    minV = 1000000000000000
    dfs(0, 0)
    print('#{} {}'.format(tc, minV-B))