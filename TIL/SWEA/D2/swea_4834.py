import sys

sys.stdin = open('4834.txt')

T = int(input())
for tc in range(1, T+1):
    N  = int(input())
    numbers = list(map(int, input()))
    cntlst = [0] * 10

    for i in numbers:
        cntlst[i] = cntlst[i] + 1

    p = 0
    for j in range(len(cntlst)):
        if cntlst[j] >= cntlst[p]:
            p = j

    print('#{} {} {}'.format(tc, p, cntlst[p]))




