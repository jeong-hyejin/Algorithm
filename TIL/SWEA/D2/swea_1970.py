import sys
sys.stdin = open('input_1970.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    print('#{}'.format(tc))
    cnt = 0
    for i in lst:
        cnt = N // i
        print(cnt,end=" ")
        N = N - (i*cnt)
    print()