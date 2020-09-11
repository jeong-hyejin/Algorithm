T = int(input())
for tc in range(1,T+1):
    print('#{}'.format(tc))
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도 회전 배열 만들기
    arr_90 = [[0] * N for _ in range(N)]
    # 원배열에서 3열부터 1행까지의 순서로 arr_90에 하나씩 넣어준다
    # ex) arr_90[0][0] <- arr[3][0]값을 넣기
    for y in range(N):
        for x in range(N):
            arr_90[y][x] = arr[N-x-1][y]

    # 180도 회전 배열 만들기
    arr_180 = [[0] * N for _ in range(N)]
    # 원배열을 이제 arr_90배열로 똑같이 적용
    for y in range(N):
        for x in range(N):
            arr_180[y][x] = arr_90[N-x-1][y]

    # 270도 회전 배열 만들기
    arr_270 = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            arr_270[y][x] = arr_180[N-x-1][y]

    # print(arr_90, arr_180, arr_270)
    for i in range(N):
    # 리스트의 값을 공백없이 출력
        print(*arr_90[i], sep="", end=" ")
        print(*arr_180[i], sep="", end=" ")
        print(*arr_270[i], sep="")