def perm(k, cur_sum):
    global minV
    if cur_sum > minV:
        return
    if k == N:
        minV = min(minV, cur_sum)
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k+1, cur_sum + arr[k][cols[k]])
            cols[k], cols[i] = cols[i], cols[k]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 열의 인덱스가 담긴 리스트
    cols = [i for i in range(N)]
    minV = 10000
    perm(0, 0)
    print('#{} {}'.format(tc, minV))