import sys
sys.stdin = open('input_1210.txt')
'''
고려할 조건
1. 2가 나온 지점이 시작점이 되고 위로 올라가면서 ladder[0][c] -> c 찾기
2. 현재 위치에서 좌, 우에 1이 있는지 확인하기
3. 이동할 때 벽인지
'''
T = 10
for tc in range(1, T+1):
    print('# {}'.format(tc), end=" ")
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 고려할 조건 1번.
    # 2는 무조건 마지막 줄에 있으므로 r을 99로 고정시켜둔다.
    r = 99
    # c를 담을 변수를 만든다.
    c = 0
    # 100 * 100 사다리니까 행이 99인 줄에서 100개의 값을 순회하며
    for i in range(100):
        # 값이 2인 것을 찾아내고 c에 담는다.
        if ladder[r][i] == 2:
            c = i
    # -> 시작점은 ladder[r][c]가 된다.

    # 고려할 조건 2번.
    while r >= 0:
        # 현재값을 0으로 바꿔준다!
        ladder[r][c] = 0
        # 좌측에 1이 있는지 확인
        # 열이 0 ~ 99 까지니까 좌측으로 갈수록 c-1이 되고 그 값이 0보다 작으면 안된다.
        # 만약 ladder[r][c-1]이 1이라면 c에 1씩 빼주면서 좌측으로 이동한다.
        if c-1 >= 0 and ladder[r][c-1] == 1:
            c -= 1
            # continue를 해주는 이유는 만일 ladder[r][c-1]값과 ladder[r][c+1] 모두 1이였을때,
            # 어느 방향으로 갈지 길을 잃게 된다.
            # 그래서 현재 있는 위치에서 좌 또는 우측으로 이동했을 때 이동하기 전의 값을 0으로 바꿔준다.
            continue
        # 우측에 1이 있는지 확인
        # 열이 0 ~ 99 까지니까 우측으로 갈수록 c+1이 되고 그 값이 99보다 크면 안된다.
        # 만약 ladder[r][c+1]이 1이라면 c에 1씩 더해주면서 우측으로 이동한다.
        if c+1 <= 99 and ladder[r][c+1] == 1:
            c += 1
            continue
        # 좌, 우측 모두 1이 없다면 위로 이동한다.
        else:
            r -= 1
    print(c)