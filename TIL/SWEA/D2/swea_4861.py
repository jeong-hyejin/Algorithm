'''
N * N table에서 길이가 M인 회문을 찾는 문제
여기서 주의할 점은 N과 M이 같지않을때,
만약 10 * 10 table에서 길이가 5인 회문이라면
['ABCDEFGHIJ']에서 시작점의 범위는 'A'~'F'까지만 확인하면 된다.!
-> 범위를 N-M+1로 주어야 한다.!
'''
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))

    # 행 체크
    for i in range(N):
        for j in range(N-M+1):
            # 회문 길이만큼 슬라이싱해서 [::-1]과 같다면,
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                # 출력한다.
                print(arr[i][j:j+M])
    # 열 체크
    # 열 체크를 할 땐 슬라이싱을 사용할 수 없다.
    # 열을 그냥 새로운 리스트에 담아서 위와 같은 방법을 사용하자.

    # 2차원 배열을 담을 리스트를 만든다.
    colunm = []
    # 완전탐색을 이용하여 열 값을 lst리스트에 담아준다.
    for i in range(N):
        lst = []
        for j in range(N):
            lst.append(arr[j][i])
        # [ [""], [""], [""].... ]
        colunm.append(lst)

    # 행 체크 방법과 동일하게 적용한다.
    for i in range(N):
        for j in range(N-M+1):
            if colunm[i][j:j+M] == colunm[i][j:j+M][::-1]:
                # 리스트이기때문에 str로 변환해서 출력해야 한다!
                print("".join(colunm[i][j:j+M]))