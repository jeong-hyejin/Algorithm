import sys
sys.stdin = open('input_1979.txt')

T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    # cnt = 0
    for i in range(0, N):
        cnt = 0
        for j in range(0, N):
            if arr[i][j] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
                continue
            else:
                cnt += 1
        if cnt == K:
            result += 1

    for i in range(0, N):
        cnt = 0
        for j in range(0, N):
            if arr[j][i] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
                continue
            else:
                cnt += 1
        if cnt == K:
            result += 1

    print('#{} {}'.format(tc, result))