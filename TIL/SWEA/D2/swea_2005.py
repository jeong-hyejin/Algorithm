import sys
sys.stdin = open('input_2005.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [ [] for _ in range(N)]

    arr[0].append(1)
    if len(arr) > 1:
        arr[1].append(1)
        arr[1].append(1)


    for i in range(1, N-1):
        for j in range(0, len(arr[i])-1):
            x = arr[i][j] + arr[i][j+1]
            arr[i+1].append(x)
        arr[i+1].insert(0, 1)
        arr[i+1].insert(len(arr[i+1]), 1)

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(0, len(arr[i])):
            print(arr[i][j], end=" ")
        print()