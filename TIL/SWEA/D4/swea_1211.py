import sys
sys.stdin = open('input_1211.txt')

def find(c):
    r = 0
    cnt = 0
    while r < 100:
        if c - 1 >= 0 and ladder[r][c - 1] and (moved == 0 or moved == -1):
            c -= 1
            moved = -1
        elif c + 1 <= 99 and ladder[r][c + 1] and (moved == 0 or moved == 1):
            c += 1
            moved = 1
        else:
            r += 1
            moved = 0
        cnt += 1
    return cnt


for tc in range(1, 11):
    print('#{}'.format(tc), end=" ")
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = 0
    c_list = []
    for i in range(100):
        if ladder[r][i] == 1:
            c_list.append(i)
    cnt_list = []
    result = {}

    for c in c_list:
        moved = 0
        cnt = find(c)
        result[c] = cnt
    minV = 1000
    for k, v in result.items():
        if minV > v:
            minV = v
            minK = k
    print(minK)
