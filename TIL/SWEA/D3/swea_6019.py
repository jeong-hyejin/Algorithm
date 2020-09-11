T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 총 거리 / (A기차 속력 + B기차 속력) -> 파리 이동 시간
    # 파리 이동 거리 = 파리 속력 * 파리 이동 시간
    ans = (D / (A + B)) * F
    print('#{} {}'.format(tc, ans))