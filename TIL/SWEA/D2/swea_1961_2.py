T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 처음부터 arr을 reverse
    arr.reverse()
    # 90도 회전, 180, 270도 회전값을 담을 리스트
    lst = []
    lst1 = []
    lst2 = []

    # 90도 회전
    # reverse된 arr에서 열 순회로 값을 ans에 담고 90도 리스트에 append
    for i in range(N):
        ans = ''
        for j in range(N):
            ans += str(arr[j][i])
        lst.append(ans)

    # 180도 회전
    # reverse된 arr에서 행 순회하되 열을 뒤에서부터 ans에 담고 리스트에 append
    for i in range(N):
        ans = ''
        for j in range(N-1, -1, -1):
            ans += str(arr[i][j])
        lst1.append(ans)

    # 270도 회전
    # reverse된 arr에서 열순회하되 열과 행 모두 뒤에서부터 ans에 담고 리스트에 append
    for i in range(N-1, -1, -1):
        ans = ''
        for j in range(N-1, -1, -1):
            ans += str(arr[j][i])
        lst2.append(ans)

    # 각각의 리스트에 첫번째 요소부터 하나씩 출력
    for i in range(N):
        print(lst[i], lst1[i], lst2[i], end=" ")
        print()