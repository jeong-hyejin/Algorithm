import sys
sys.stdin = open('input_1209.txt')
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    '''
    4 4 3 2 1
    2 2 1 6 5
    3 5 4 6 7
    4 2 5 9 7
    8 1 9 5 6
    '''
    # row, column
    total_list = []
    for i in range(100):
        row_total = 0
        column_total = 0
        for j in range(100):
            row_total += arr[i][j]
            column_total += arr[j][i]
        total_list.append(row_total)
        total_list.append(column_total)
    # row_diagonal, column_diagonal
    row_diagonal_total = 0
    column_diagonal_total = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                row_diagonal_total += arr[i][j]
        column_diagonal_total += arr[i][4-i]
    total_list.append(row_diagonal_total)
    total_list.append(column_diagonal_total)

    max_num = 0
    for i in total_list:
        if max_num < i:
            max_num = i
    print('#{} {}'.format(tc, max_num))