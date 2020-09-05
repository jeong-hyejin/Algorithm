import sys

sys.stdin = open('4835.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    num_list = []
    for i in range(N - M + 1):
        result = 0
        for j in range(M):
            result += numbers[i + j]
        num_list.append(result)

    min_num = num_list[0]
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print('#{} {}'.format(tc, max_num - min_num))