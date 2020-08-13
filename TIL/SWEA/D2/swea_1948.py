import sys
sys.stdin = open('input_1948.txt')

T = int(input())
for tc in range(1, T+1):

    lst = list(map(int, input().split()))

    num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in num[lst[0]:lst[2]-1]:
        total += i

    if lst[0] == lst[2]:
        total += (lst[3] - lst[1])
    else: 
        total += (num[lst[0]-1] - lst[1]) + lst[3]
    print('#{} {}'.format(tc, total+1))