T = int(input())
for tc in range(1, T+1):

    arr = [[0] * 10 for i in range(10)]
    N = int(input())
    count = 0
    for i in range(N):
        A = list(map(int, input().split()))
        for j in range(A[0], A[2]+1):
            for k in range(A[1], A[3]+1):
                arr[j][k] += A[4]

                if arr[j][k] == 3:
                    count += 1
    print('#{} {}'.format(tc, count))