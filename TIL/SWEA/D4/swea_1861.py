def isWall(y, x):
    if y >= 0 and y < N and x >= 0 and x < N:
        return True
    return False

import sys
sys.stdin = open('input_1861.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    Q = []
    max_cnt = 0
    cur_num = 10000
    for y in range(N):
        for x in range(N):
            cnt = 0
            Q.append((y, x))
            while Q:
                curY, curX = Q.pop(0)
                for d in range(4):
                    newY = curY + dy[d]
                    newX = curX + dx[d]
                    if isWall(newY, newX) and arr[newY][newX] == arr[curY][curX] + 1:
                        cnt += 1
                        Q.append((newY, newX))
            if max_cnt < cnt:
                max_cnt = cnt
                cur_num = arr[y][x]
            if max_cnt == cnt:
                if cur_num > arr[y][x]:
                    cur_num = arr[y][x]
    print('#{} {} {}'.format(tc, cur_num, max_cnt+1))