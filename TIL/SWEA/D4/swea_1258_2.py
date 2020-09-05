T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for r in range(0, N)]
    cnt = 0 # 행렬의 갯수를 담는 변수
    ans = [] # 답을 담을 변수
    for r in range(0, N) :
        for c in range(0, N) :
            if arr[r][c] != 0 : # 행렬 안에 행렬 찾기, 만약 행렬 요소값이 있으면
                cnt += 1    # 행열의 갯수
                nr = r  # 배열의 첫번째행 값을 담음
                while True : # sub 행렬의 마지막 행값을 찾기 위한 반복문
                    nr +=1
                    if nr<0 or nr >= N or arr[nr][c] == 0 : # 만약 인덱스 범위를 넘어가거나 행의 끝을 넘어가면 반복문 종료
                        break
                nc = c # 첫번째 열값 저장
                while True : # sub 행렬의 마지막 열값을 찾기 위한 반복문
                    nc += 1 # 마지막 열을 찾음
                    if nc < 0 or nc >= N or arr[r][nc] == 0 : # 만약 인덱스 범위르 넘어가거나 열의 끝을 넘어가면 반복문 종료
                        break

                for x in range(r, nr) : # 지나갔던 sub행렬이 값을 0으로 초기화시켜 없애주고 sub행렬의 행,열의 크기는 ans리스트에 저장
                    for y in range(c, nc) :
                        arr[x][y] = 0
                ans.append((nr-r, nc-c))

    for i in range(0, cnt) : # cnt = 행렬의 갯수
        min_i = i
        for j in range(i+1, cnt):
            if ans[min_i][0]*ans[min_i][1] > ans[j][0] * ans[j][1] : # 행렬의 크기가 더 작은 값이 앞으로 가게
                min_i = j
        ans[min_i], ans[i] = ans[i], ans[min_i]
    print(f'#{test_case} {cnt}', end = ' ')
    for r, c in ans :
        print(f'{r} {c}', end = ' ')
    print()