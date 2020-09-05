def pe(k, midSum):
    # 기본적으로 전역변수는 어디에서나 읽을 수 있지만, 함수 안에서 전역변수에 새로운 값을 '대입'하는 것은 불가능하다.
    # golbal 키워드를 사용하면 전역변수에 새로운 값을 대입할 수 있다.
    global minV
    # 최솟값을 구하는 문제이므로 행이 끝나지 않았는데 요소의 합이 최솟값보다 크다면 그냥 리턴
    if midSum > minV:
        return
    # 배열을 다 돌았다면 (마지막 행까지 돌았다면)
    if k == N:
        # 각 행에서 하나씩 뽑아 더한 값(midSum)이 최솟값(minV)보다 작다면
        # minV는 sumV이 된다.
        if midSum < minV:
            minV = midSum
        return minV
    else:
        # column 개수만큼 반복을 돌면서
        for i in range(N):
            # column의 요소가 방문하지 않았던 요소라면
            if not visited[i]:
                # 방문설정을 해주고
                visited[i] = True
                # 다음 행으로 넘겨주고 midSum에 요소를 더한 값도 넘겨준다.
                pe(k+1, midSum + arr[k][i])
                # visited를 초기화
                visited[i] = False
    # for문이 끝나면 return
    return minV
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    minV = 10000
    print('#{} {}'.format(tc, pe(0, 0)))