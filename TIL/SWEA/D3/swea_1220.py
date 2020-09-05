'''
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''
import sys
sys.stdin = open('input_1220.txt')
T = 10
for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    trans = list(zip(*table))
    cnt = 0
    for i in trans:
        start = 0
        for j in i:
            if j == 1:
                start = 1
            if j == 2 and start == 1:
                cnt += 1
                start = 0
    print('#{} {}'.format(tc, cnt))

# N = int(input())
# table = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# for r in range(N):
#     for c in range(N):
#         if table[r][c] == 1:
#             while r < N-1:
#                 r += 1
#                 if table[r][c] == 2:
#                     cnt += 1
#                     break
#     if r == 6:
#            continue
# print(cnt)