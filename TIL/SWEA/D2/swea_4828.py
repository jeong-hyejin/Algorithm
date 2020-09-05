import sys

sys.stdin = open('4828.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = numbers[0]
    min_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i

    for j in numbers:
        if j <= min_num:
            min_num = j

    print('#{} {}'.format(tc, max_num - min_num))