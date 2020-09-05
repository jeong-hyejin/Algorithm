T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    result = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                cnt += 1
                sr = r
                while True:
                    sr += 1
                    if sr < 0 or sr >= N or arr[sr][c] == 0:
                        break
                sc = c
                while True:
                    sc += 1
                    if sc < 0 or sc >= N or arr[r][sc] == 0:
                        break
                for y in range(r, sr):
                    for x in range(c, sc):
                        arr[y][x] = 0
                result.append(((sr-r) * (sc-c),sr-r, sc-c))
                result.sort()
    print(len(result), end=" ")
    for i in result:
        print(i[1], i[2], end= " ")
    print()