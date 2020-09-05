# BOJ 단지번호, 배추밭

import sys
sys.stdin = open('input_4615.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    i = N // 2
    j = i - 1
    arr[i][i] = 2
    arr[j][j] = 2
    arr[i][j] = 1
    arr[j][i] = 1

    for i in range(M):
        x, y, color = map(int, input().split())
        # arr의 인덱스는 0부터 시작하니까 -1을 빼준다.
        x = x - 1
        y = y - 1
        arr[y][x] = color
        # 오른쪽, 왼쪽, 아래, 위, 대각선오른쪽아래, 대각선왼쪽아래, 대각선 오른쪽위, 대각선 왼쪽위
        dx = [1, -1, 0, 0, 1, -1, 1, -1]
        dy = [0, 0, 1, -1, 1, 1, -1, -1]
        for d in range(8):
            newX = x + dx[d]
            newY = y + dy[d]
            # 방향을 이동한 값(오른쪽으로 이동했다면 오른쪽으로 이동한 값)이 현재의 color와 같지 않다면,
            # 현재의 color와 같은 값이 나올때까지 이동
            while newX >= 0 and newY >= 0 and newX < N and newY < N and arr[newY][newX] != 0 and arr[newY][newX] != color:
                newX += dx[d]
                newY += dy[d]
            # 쭉 이동하다가 color가 같은 값을 만났다면,
            # 맨 처음 위치로 다시 되돌아오면서 값을 바꿔준다. ex) 1 2 2 1 -> 1 1 1 1
            if newX >= 0 and newY >= 0 and newX < N and newY < N and arr[newY][newX] == color:
                while newX >= 0 and newY >= 0 and newX < N and newY < N and x != newX or y != newY:
                    newX -= dx[d]
                    newY -= dy[d]
                    arr[newY][newX] = color

    cnt = 0
    cnt1 = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 2:
                cnt1 += 1
    print('#{} {} {}'.format(tc, cnt, cnt1))