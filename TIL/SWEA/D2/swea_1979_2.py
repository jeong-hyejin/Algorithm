'''
한 줄씩 탐색하면서 0이면 1이 나올때까지 옆으로 이동한다.
1이 나오면 0이 나올때까지 쭉 이동하며 cnt를 센다.
0이 나오면 cnt를 다시 초기화하고 1이 나올때까지 이동 -> 1이 나오면 0이 나올때까지 cnt세며 이동하는것을 반복!
'''

'''
초기화를 어디에서 할 지,
소스코드가 돌아가는 순서를 익혀야겠다.
'''

import sys
sys.stdin = open('input_1979.txt')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    totalcnt = 0
    for i in range(N):
        # 가로
        j = 0
        while j < N:
            while j < N and arr[i][j] == 0:
                j += 1
            cnt = 0 # cnt 초기화
            while j < N and arr[i][j] == 1:
                j += 1
                cnt += 1
            if cnt == K:
                totalcnt += 1
        # 세로
        j = 0
        while j < N:
            while j < N and arr[j][i] == 0:
                j += 1
            cnt = 0 # cnt 초기화
            while j < N and arr[j][i] == 1:
                j += 1
                cnt += 1
            if cnt == K:
                totalcnt += 1
    print('#{} {}'.format(tc, totalcnt))